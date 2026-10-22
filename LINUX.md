# Linux and Proton

This release contains Windows x64 executables. It does not contain a native Linux application build.

For Proton, extract the whole Windows ZIP into one directory. Add **NX Infinity.exe** to Steam as a non-Steam game, enable a Proton compatibility tool in its properties, and keep the supporting core folders intact. Use one consistent prefix so configuration and saves remain available.

The archive contains `docs/proton/README.md`, `probe.py`, and `verify_release.py` with environment checks, setup details and package verification. Controller receiver devices must be available to the host; Steam Input and a receiver's XInput mode can affect how the controller appears.

Package integrity checks have run on Windows and Ubuntu under WSL. WSL package checks do not establish Proton gameplay compatibility. Actual Proton/Wine gameplay, Linux graphics-driver behavior and Steam Deck operation remain unverified.

If reporting a problem, include distribution, Proton version, GPU/driver, selected core and the application's diagnostic report. Review reports for private information before posting.
