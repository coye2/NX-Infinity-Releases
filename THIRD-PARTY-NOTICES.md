# Third-party notices — NX Infinity 1.0.0-beta.1

The original NX API source is offered under the MIT license, subject to notices on individual files. Its MIT license does **not** change the licenses of the native emulator implementations, their modifications, or their dependencies.

This public notice accompanies the [upstream credits and complete recorded dependency inventory](THIRD-PARTY-CREDITS.md). It does **not** yet establish clearance for publicly distributing the Windows package, and it does not replace original license text in any download. The existing API Source ZIP must be amended because its LICENSE refers to this notice but its standalone ZIP omits the notice.

## Original emulation implementations

| Implementation | Pinned source | Applicable upstream license and attribution |
|---|---|---|
| Kenji-NX / Ryujinx | [Kenji-NX original source](https://starforgejo.dev/projects/Kenji-NX), commit `7d1fd99d3dc1c230ef7f823e96f187b3de619e4a` | MIT, original Ryujinx/Kenji contributor notices, LibHac/dependency notices |
| Ryujinx Canary / Ryubing lineage | commit `7f0e82fe481ce9c2cb6eb57e63171421254d2c6b` | MIT and original third-party notices, including LibHac |
| Eden | [Eden mirror](https://github.com/eden-emulator/mirror/tree/de7e6e01d43e8cf2ec193d74fa053b0d7949955f) | GPL-3.0-or-later with inherited source-file notices; NX worker links core code directly |
| Citron Neo | [Citron original source](https://github.com/citron-neo/emulator/tree/598b700884c7cd3bee0a25ce30d0cab066117c5b) | GPL-3.0-or-later with inherited yuzu/Citra source notices; NX worker links core code directly |

## Multimedia and other components

| Component | Recorded package/build | Original rights/license notes |
|---|---|---|
| FFmpeg for Ryujinx native video decoder | `Ryujinx.Graphics.Nvdec.Dependencies.Windows 6.1.2-build4` | NuGet declares LGPL-2.1-only. Actual FFmpeg build flags and full corresponding source need confirmation. See [FFmpeg legal information](https://ffmpeg.org/legal.html). |
| FFmpeg for Eden | CI package `9.0.2-1790726865-946fcce07b` for LLVM-MinGW static build | Incomplete component/source correspondence for this exact static input; FFmpeg license may vary by enabled codecs and build flags. |
| OpenAL Soft | `Ryujinx.Audio.OpenAL 1.24.3` with `OpenAL32.dll` | NuGet declares LGPL-2.0-only, original upstream [OpenAL Soft](https://github.com/kcat/openal-soft) license. Versioned source/build correspondence remains unverified. |
| SDL2/SDL3 | SDL3-CS `2026.918.0`; Eden SDL3 and Citron SDL2 from source | [SDL zlib license](https://www.libsdl.org/license.php); original SDL contributors and SDL3-CS ppy Pty Ltd copyright |
| .NET Runtime and front-end libraries | .NET 10.0.13; Avalonia, SkiaSharp, HarfBuzzSharp, Inter, MicroCom, Lucide and others | Original recorded MIT/OFL/ISC/component notices apply. See [credits inventory](THIRD-PARTY-CREDITS.md). |
| Citron related build-time and linked libraries | Boost, OpenSSL, FFmpeg, SDL2, libnx-related fixtures and source dependencies | Retain notices and corresponding-source obligations for the actual shipped source/link closure, not only component names. |

## Redistribution/source availability — still pending

1. Publish **complete corresponding source** for the exact modified GPL-covered Eden and Citron native worker binaries, including NX integration, overlaid/patched sources, applicable linked-library source, build scripts and full license notices. The rest of NX Infinity's private repository does not automatically need to be published merely because these separately running workers are GPL, but the precise source boundary requires verification.
2. For FFmpeg and OpenAL native binaries, supply matching source, modifications, build/configuration provenance, original license texts and the LGPL materials required for dynamic/static linking and relinking where applicable. Validate that no incompatible or nonredistributable FFmpeg configuration was used.
3. Verify the final per-file Windows payload, notices, and exact native-dependency provenance from the archived package—not just historical development build inventories.
4. Amend the **standalone API Source ZIP** to include this notice or an accurate equivalent, update its SOURCE-BUILD inventory and new public ZIP/checksum provenance. Preserve the original ZIP.
5. Keep the release as a draft until these conditions are met. Names/credits on this page are not themselves proof of license compliance.

The project does not bundle Nintendo games, firmware, private keys or Nintendo SDK material according to its existing release validation. Upstream names and marks are used solely for attribution; no endorsement is implied.
