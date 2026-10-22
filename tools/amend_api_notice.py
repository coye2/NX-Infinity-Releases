#!/usr/bin/env python3
"""Amend the beta.1 MIT API source export with its missing notice, without rebuilding or overwriting."""
import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile, ZIP_DEFLATED

TAG = "v1.0.0-beta.1"
REPO = "coye2/NX-Infinity-Releases"
STEM = "NX-Infinity-1.0.0-beta.1"
NOTICE_URL = (
    "https://raw.githubusercontent.com/coye2/NX-Infinity-Releases/"
    "94e1dd2eb8be4a0f1b7ad1bd67486d684d5f2c9e/THIRD-PARTY-NOTICES.md"
)
EXPECTED_COMMIT = "e62e5e582c7e400531f66bbac97ec2ded076e455"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def record(data):
    return {"bytes": len(data), "sha256": sha(data)}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=Path.cwd())
    parser.add_argument("--upload-draft", action="store_true")
    args = parser.parse_args()
    root = args.directory.resolve(strict=True)
    old_file = root / f"{STEM}-API-Source.zip"
    new_file = root / f"{STEM}-API-Source-Notices.zip"
    provenance = root / f"{STEM}-API-Notices-SHA256.json"
    if not old_file.is_file():
        raise SystemExit(f"Original API ZIP absent: {old_file}")
    if new_file.exists() or provenance.exists():
        raise SystemExit("Corrected output already exists; refusing to overwrite anything.")
    with urlopen(NOTICE_URL, timeout=30) as response:
        notice = response.read()
    if not notice.startswith(b"# Third-party notices"):
        raise SystemExit("Unexpected upstream notice response")

    with ZipFile(old_file) as src:
        if src.testzip() is not None:
            raise SystemExit("Original API ZIP is corrupt")
        infos = [i for i in src.infolist() if not i.is_dir()]
        names = [i.filename for i in infos]
        if len(names) != len(set(names)):
            raise SystemExit("Duplicate API archive entries")
        if any(not n.startswith("NX-API/") or ".." in n.split("/") or "\\" in n for n in names):
            raise SystemExit("Unexpected archive path")
        original = {i.filename: src.read(i) for i in infos}
        receipt_name = "NX-API/SOURCE-BUILD.json"
        receipt = json.loads(original[receipt_name])
        if receipt.get("sourceCommit") != EXPECTED_COMMIT:
            raise SystemExit("API source commit differs from the release candidate")
        old_inventory = dict(receipt["files"])
        from_zip = {key[7:]: record(data) for key, data in original.items() if key != receipt_name}
        if old_inventory != from_zip:
            raise SystemExit("Existing API SOURCE-BUILD inventory differs from the ZIP")
        notice_name = "NX-API/THIRD-PARTY-NOTICES.md"
        if notice_name in original:
            raise SystemExit("API notice is already present; no amendment needed")
        receipt["files"]["THIRD-PARTY-NOTICES.md"] = record(notice)
        receipt["publicationAmendment"] = {
            "kind": "documentation-only",
            "description": "Add the referenced third-party notice to standalone API source.",
            "originalInventoryCount": len(old_inventory),
            "codeFilesUnchanged": True,
            "noticeSha256": sha(notice),
            "originalBuildReceiptPreserved": True,
            "independentRebuildPerformed": False
        }
        updated_receipt = (json.dumps(receipt, indent=2) + "\n").encode("utf-8")
        with ZipFile(new_file, "x", compression=ZIP_DEFLATED, compresslevel=4) as out:
            for item in infos:
                if item.filename == receipt_name:
                    out.writestr(item, updated_receipt)
                else:
                    out.writestr(item, original[item.filename])
            out.writestr(notice_name, notice)

    with ZipFile(new_file) as verify:
        if verify.testzip() is not None:
            raise SystemExit("Corrected ZIP failed integrity check; do not upload")
        files = {i.filename: verify.read(i) for i in verify.infolist() if not i.is_dir()}
        if set(files) != set(original) | {notice_name}:
            raise SystemExit("Corrected ZIP has extra or missing files")
        if any(files[name] != data for name, data in original.items() if name != receipt_name):
            raise SystemExit("Original API code or documentation changed")
        sealed = json.loads(files[receipt_name])
        actual = {key[7:]: record(data) for key, data in files.items() if key != receipt_name}
        if sealed.get("files") != actual:
            raise SystemExit("Amended inventory does not match the ZIP")
    old_bytes = old_file.read_bytes()
    new_bytes = new_file.read_bytes()
    prior_sha = sha(old_bytes)
    if prior_sha != "4c74cba7b4a87504183e4e56a8b02bedd35d918047b9aae41ece52494d60418b":
        raise SystemExit("Original API hash changed; do not upload")
    report = {
        "sourceCommit": EXPECTED_COMMIT, "scope": "documentation-only API source export notice correction",
        "original": {"file": old_file.name, **record(old_bytes)},
        "amended": {"file": new_file.name, **record(new_bytes)},
        "upstreamNotice": {"source": NOTICE_URL, **record(notice)},
        "originalCodeFilesUnchanged": True,
        "independentAPIRebuildPerformedForAmendment": False,
        "replacesOriginalAsset": False
    }
    with provenance.open("x", encoding="utf-8") as target:
        json.dump(report, target, indent=2)
        target.write("\n")
    print(f"Corrected archive: {new_file.name}, {len(new_bytes)} bytes, sha256:{sha(new_bytes)}")
    print(f"Additional checksum/provenance: {provenance.name}")
    print("Original API ZIP untouched; original SOURCE-BUILD code inventory verified.")

    if args.upload_draft:
        gh = shutil.which("gh")
        if not gh:
            raise SystemExit("GitHub CLI not installed; corrected files remain local.")
        info = subprocess.run([gh, "release", "view", TAG, "-R", REPO, "--json", "isDraft,assets"],
                              capture_output=True, text=True, check=True)
        release = json.loads(info.stdout)
        if release.get("isDraft") is not True:
            raise SystemExit("Release is not a draft; refusing upload.")
        existing = {asset["name"] for asset in release["assets"]}
        if {new_file.name, provenance.name} & existing:
            raise SystemExit("Corrected asset name already exists remotely; refusing overwrite.")
        subprocess.run([gh, "release", "upload", TAG, str(new_file), str(provenance), "-R", REPO],
                       check=True)
        print("Uploaded amended API ZIP and provenance to GitHub DRAFT. No assets replaced.")
        print("This does not resolve the separate native GPL/LGPL source obligations.")

if __name__ == "__main__":
    main()
