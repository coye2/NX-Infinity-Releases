# NX Infinity beta.1 — upstream credits and dependency attribution

**Source candidate:** `e62e5e582c7e400531f66bbac97ec2ded076e455` · **Prepared:** 2026-10-22 · **Status:** attribution inventory, NOT redistribution clearance.

NX Infinity builds on community-made software. **All original projects, contributors, copyright holders, applicable license grants, and attribution notices remain credited.** NX Infinity is not sponsored or endorsed by any of these upstream projects or by Nintendo. The names below are projects or recorded authors, not an exhaustive roster of individual contributors; original license files and per-file copyright notices take precedence.

**Important:** this file credits all *identified* projects and package records available in the reviewed source manifest. The final executable-to-package provenance audit remains incomplete for certain native assets; therefore it must not be described as proof that every contributor or legal notice has been identified. The Windows binary must not be publicly distributed solely on the strength of this credits list.

## Core code, original creators, and foundational technologies

| Component | Exact recorded pin / version | Original license | Upstream / source | Rights holders and credit |
|---|---|---|---|---|
| Kenji-NX / Ryujinx family | 7d1fd99d3dc1c230ef7f823e96f187b3de619e4a | MIT; additional third-party obligations | [source](https://starforgejo.dev/projects/Kenji-NX) | Kenji-NX team, historical Ryujinx contributors, and original copyright holders; NX applies recorded patches |
| Ryujinx Canary / Leuconoe-Ryubing lineage | 7f0e82fe481ce9c2cb6eb57e63171421254d2c6b | MIT; original notices | [source](https://starforgejo.dev/archive/Leuconoe_Ryubing) | Historical Ryujinx, Ryubing and Leuconoe contributors; original notices retained |
| LibHac for Canary | 23e402ebb6dedc517e34a98a033078dc0f6fd478 | MIT / ISC / BSD notices | [source](https://starforgejo.dev/archive/LibHac_Ryubing) | Alex Barney, hactool contributors, XTSSharp rights holders and LibHac contributors |
| Eden | de7e6e01d43e8cf2ec193d74fa053b0d7949955f | GPL-3.0-or-later with inherited per-file notices | [source](https://github.com/eden-emulator/mirror) | Eden Emulator Project, inherited yuzu/Citra contributors, and holders identified in individual files |
| Citron Neo | 598b700884c7cd3bee0a25ce30d0cab066117c5b | GPL-3.0-or-later with inherited per-file notices | [source](https://github.com/citron-neo/emulator) | Citron Neo, inherited yuzu/Citra contributors, and holders identified in individual files |
| FFmpeg: Kenji native decoder DLLs | 6.1.2-build4 NuGet package | NuGet metadata: LGPL-2.1-only; actual compile options unverified | [source](https://ffmpeg.org/) | FFmpeg developers and included codecs' third-party authors |
| OpenAL Soft: Kenji OpenAL32.dll | 1.24.3 NuGet package | NuGet metadata: LGPL-2.0-only; actual source/build recipe unverified | [source](https://github.com/kcat/openal-soft) | OpenAL Soft developers and original copyright holders |
| SDL3 native + SDL2 | SDL3-CS 2026.918.0; Eden SDL 3.4.8; Citron SDL2 | zlib, preserve original provenance | [source](https://github.com/libsdl-org/SDL) | SDL contributors; ppy Pty Ltd for SDL3-CS managed binding |
| .NET runtime and libraries | Microsoft.NETCore.App.Runtime.win-x64 10.0.13 | MIT and separately bundled third-party notices | [source](https://github.com/dotnet/dotnet) | Microsoft, .NET Foundation, and third-party runtime copyright holders |
| Inter typeface | bundled asset; exact embedded version not independently established | SIL Open Font License 1.1 | [source](https://github.com/rsms/inter) | Rasmus Andersson and other original Inter contributors |
| Lucide icons | recorded in frontend license/source-provenance files | ISC (review original versioned notice) | [source](https://github.com/lucide-icons/lucide) | Lucide contributors and upstream icon creators |
| shaderc, SPIR-V, glslang | versioned original shaderc license records | various original licenses; retained in core stage | [source](https://github.com/google/shaderc) | Google, Khronos and listed upstream copyright holders |
| NX API and integration contributions | 1.0.0-beta.1 candidate | MIT for original API; GPL for Eden/Citron native combined workers | [source](https://github.com/coye2/NX-Infinity-Releases) | NX API contributors; keep copyright notices from all upstream works |

## Frontend resolved package inventory

Source: the private candidate's `apps/NxInfinity/dependencies.json`, with 27 packages, locked for the frontend. **This is the full restore graph, not a statement that each row ships in the Windows ZIP**; build-only and non-Windows packages must not be mislabeled as distributed binaries. The authoritative packaged-file index is separate. Keep the actual original license/notice texts with each distributed applicable component.

| Package | Recorded version | Recorded author | Recorded license | Source reference |
|---|---|---|---|---|
| Avalonia.Desktop | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| Avalonia.Fonts.Inter | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| Avalonia.Themes.Fluent | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| Microsoft.NET.ILLink.Tasks | 10.0.13 | not recorded | MIT | [source](https://github.com/dotnet/dotnet) |
| Avalonia | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| Avalonia.Angle.Windows.Natives | 2.1.27548.20260419 | not recorded | LICENSE | [source](https://github.com/AvaloniaUI/angle/) |
| Avalonia.BuildServices | 11.3.2 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia.BuildServices) |
| Avalonia.FreeDesktop | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| Avalonia.FreeDesktop.AtSpi | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| Avalonia.HarfBuzz | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| Avalonia.Native | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| Avalonia.Remote.Protocol | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| Avalonia.Skia | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| Avalonia.Win32 | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| Avalonia.X11 | 12.1.4 | not recorded | MIT | [source](https://github.com/AvaloniaUI/Avalonia/) |
| HarfBuzzSharp | 8.3.1.3 | not recorded | MIT | [source](https://go.microsoft.com/fwlink/?linkid=868515) |
| HarfBuzzSharp.NativeAssets.Linux | 8.3.1.3 | not recorded | MIT | [source](https://go.microsoft.com/fwlink/?linkid=868515) |
| HarfBuzzSharp.NativeAssets.macOS | 8.3.1.3 | not recorded | MIT | [source](https://go.microsoft.com/fwlink/?linkid=868515) |
| HarfBuzzSharp.NativeAssets.WebAssembly | 8.3.1.3 | not recorded | MIT | [source](https://go.microsoft.com/fwlink/?linkid=868515) |
| HarfBuzzSharp.NativeAssets.Win32 | 8.3.1.3 | not recorded | MIT | [source](https://go.microsoft.com/fwlink/?linkid=868515) |
| MicroCom.Runtime | 0.11.6 | not recorded | MIT | [source](https://github.com/kekekeks/MicroCom) |
| SkiaSharp | 3.119.4 | not recorded | MIT | [source](https://go.microsoft.com/fwlink/?linkid=868515) |
| SkiaSharp.NativeAssets.Linux | 3.119.4 | not recorded | MIT | [source](https://go.microsoft.com/fwlink/?linkid=868515) |
| SkiaSharp.NativeAssets.macOS | 3.119.4 | not recorded | MIT | [source](https://go.microsoft.com/fwlink/?linkid=868515) |
| SkiaSharp.NativeAssets.WebAssembly | 3.119.4 | not recorded | MIT | [source](https://go.microsoft.com/fwlink/?linkid=868515) |
| SkiaSharp.NativeAssets.Win32 | 3.119.4 | not recorded | MIT | [source](https://go.microsoft.com/fwlink/?linkid=868515) |
| Tmds.DBus.Protocol | 0.94.1 | not recorded | MIT | [source](https://github.com/tmds/Tmds.DBus.git) |

## Kenji / Ryujinx resolved NuGet package inventory

Source: `backends/ryujinx/dependencies-win-x64-product.json`, recording 142 package entries and 333 published-stage files. The package graph can include build-only, managed, platform-specific and runtime graph entries **not physically distributed in the beta ZIP**; do not interpret this list as evidence each one ships. “Not recorded” means no author/license field was present in *this metadata*, not that a package has no copyright/license.

| Package | Recorded version | Recorded author | NuGet metadata license | Source reference |
|---|---|---|---|---|
| Concentus | 2.2.2 | Logan Stromberg | LICENSE | [source](https://github.com/lostromb/concentus) |
| Gommon | 2.7.1.1 | GreemDev | see original license | [source](https://github.com/GreemDev/Gommon) |
| Humanizer | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.af | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.ar | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.az | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.bg | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.bn-BD | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.cs | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.da | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.de | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.el | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.es | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.fa | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.fi-FI | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.fr | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.fr-BE | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.he | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.hr | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.hu | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.hy | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.id | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.is | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.it | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.ja | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.ko-KR | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.ku | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.lv | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.ms-MY | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.mt | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.nb | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.nb-NO | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.nl | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.pl | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.pt | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.ro | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.ru | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.sk | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.sl | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.sr | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.sr-Latn | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.sv | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.th-TH | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.tr | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.uk | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.uz-Cyrl-UZ | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.uz-Latn-UZ | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.vi | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.zh-CN | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.zh-Hans | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| Humanizer.Core.zh-Hant | 2.14.1 | Mehdi Khalili, Claire Novotny | MIT | [source](https://github.com/Humanizr/Humanizer) |
| JetBrains.Annotations | 2023.2.0 | JetBrains | MIT | [source](https://github.com/JetBrains/JetBrains.Annotations.git) |
| Microsoft.CodeAnalysis.Analyzers | 3.3.4 | Microsoft | MIT | [source](https://github.com/dotnet/roslyn-analyzers) |
| Microsoft.CodeAnalysis.Common | 4.9.2 | Microsoft | MIT | [source](https://github.com/dotnet/roslyn) |
| Microsoft.CodeAnalysis.CSharp | 4.9.2 | Microsoft | MIT | [source](https://github.com/dotnet/roslyn) |
| Microsoft.CSharp | 4.7.0 | Microsoft | MIT | [source](https://github.com/dotnet/corefx) |
| Microsoft.DotNet.PlatformAbstractions | 3.1.6 | Microsoft | LICENSE.TXT | not recorded |
| Microsoft.Extensions.DependencyInjection.Abstractions | 8.0.0 | Microsoft | MIT | [source](https://github.com/dotnet/runtime) |
| Microsoft.Extensions.DependencyModel | 8.0.0 | Microsoft | MIT | [source](https://github.com/dotnet/runtime) |
| Microsoft.Extensions.Logging.Abstractions | 8.0.0 | Microsoft | MIT | [source](https://github.com/dotnet/runtime) |
| Microsoft.IdentityModel.Abstractions | 8.12.0 | Microsoft | MIT | [source](https://github.com/AzureAD/azure-activedirectory-identitymodel-extensions-for-dotnet) |
| Microsoft.IdentityModel.JsonWebTokens | 8.12.0 | Microsoft | MIT | [source](https://github.com/AzureAD/azure-activedirectory-identitymodel-extensions-for-dotnet) |
| Microsoft.IdentityModel.Logging | 8.12.0 | Microsoft | MIT | [source](https://github.com/AzureAD/azure-activedirectory-identitymodel-extensions-for-dotnet) |
| Microsoft.IdentityModel.Tokens | 8.12.0 | Microsoft | MIT | [source](https://github.com/AzureAD/azure-activedirectory-identitymodel-extensions-for-dotnet) |
| Microsoft.IO.RecyclableMemoryStream | 3.0.1 | Microsoft | MIT | [source](https://github.com/Microsoft/Microsoft.IO.RecyclableMemoryStream) |
| Microsoft.NETCore.Platforms | 1.1.0 | Microsoft | see original license | [source](https://dot.net/) |
| Microsoft.NETCore.Targets | 1.1.0 | Microsoft | see original license | [source](https://dot.net/) |
| MsgPack.Cli | 1.0.1 | FUJIWARA, Yusuke | see original license | [source](https://github.com/msgpack/msgpack-cli) |
| NetCoreServer | 8.0.7 | Ivan Shynkarenka | MIT | [source](https://github.com/chronoxor/NetCoreServer) |
| NETStandard.Library | 2.0.3 | Microsoft | see original license | [source](https://dot.net/) |
| Open.NAT.Core | 2.1.0.5 | Alan McGovern, Ben Motmans, Lucas Ontivero | see original license | [source](https://github.com/Aragas/Open.NAT.Core) |
| OpenTK.Audio.OpenAL | 4.9.4 | Team OpenTK | MIT | [source](https://github.com/opentk/opentk.git) |
| OpenTK.Core | 4.9.4 | Team OpenTK | MIT | [source](https://github.com/opentk/opentk.git) |
| OpenTK.Mathematics | 4.9.4 | Team OpenTK | MIT | [source](https://github.com/opentk/opentk.git) |
| OpenTK.redist.glfw | 3.4.0.44 | Team OpenTK | COPYING.md | [source](https://www.glfw.org/) |
| OpenTK.Windowing.GraphicsLibraryFramework | 4.9.4 | Team OpenTK | MIT | [source](https://github.com/opentk/opentk.git) |
| runtime.any.System.Globalization | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.any.System.IO | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.any.System.Reflection | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.any.System.Reflection.Primitives | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.any.System.Resources.ResourceManager | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.any.System.Runtime | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.any.System.Text.Encoding | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.any.System.Threading.Tasks | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.debian.8-x64.runtime.native.System.Security.Cryptography.OpenSsl | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.fedora.23-x64.runtime.native.System.Security.Cryptography.OpenSsl | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.fedora.24-x64.runtime.native.System.Security.Cryptography.OpenSsl | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.native.System | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.native.System.Security.Cryptography.OpenSsl | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.opensuse.13.2-x64.runtime.native.System.Security.Cryptography.OpenSsl | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.opensuse.42.1-x64.runtime.native.System.Security.Cryptography.OpenSsl | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.osx.10.10-x64.runtime.native.System.Security.Cryptography.OpenSsl | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.rhel.7-x64.runtime.native.System.Security.Cryptography.OpenSsl | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.ubuntu.14.04-x64.runtime.native.System.Security.Cryptography.OpenSsl | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.ubuntu.16.04-x64.runtime.native.System.Security.Cryptography.OpenSsl | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.ubuntu.16.10-x64.runtime.native.System.Security.Cryptography.OpenSsl | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.unix.System.Private.Uri | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.unix.System.Runtime.Extensions | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| runtime.win.System.Runtime.Extensions | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| Ryujinx.Audio.OpenAL | 1.24.3 | KeatonTheBot | LGPL-2.0-only | not recorded |
| Ryujinx.Graphics.Nvdec.Dependencies.Windows | 6.1.2-build4 | KeatonTheBot | LGPL-2.1-only | not recorded |
| Ryujinx.LibHac | 0.20.0 | Alex Barney, GreemDev | MIT | [source](https://git.ryujinx.app/ryubing/libhac.git) |
| Ryujinx.SDL3-CS | 2026.918.0 | ppy Pty Ltd | MIT | [source](https://github.com/Kenji-NX/SDL3-CS) |
| shaderc.net | 0.1.0 | Jean-Philippe Bruyère | see original license | [source](https://github.com/jpbruyere/shaderc.net.git) |
| Silk.NET.Core | 2.22.0 | .NET Foundation and Contributors | MIT | [source](https://github.com/dotnet/Silk.NET.git) |
| Silk.NET.Shaderc.Native | 2.22.0 | .NET Foundation and Contributors | Apache-2.0 | [source](https://github.com/google/shaderc) |
| Silk.NET.Vulkan | 2.22.0 | .NET Foundation and Contributors | MIT | [source](https://github.com/dotnet/Silk.NET.git) |
| Silk.NET.Vulkan.Extensions.EXT | 2.22.0 | .NET Foundation and Contributors | MIT | [source](https://github.com/dotnet/Silk.NET.git) |
| Silk.NET.Vulkan.Extensions.KHR | 2.22.0 | .NET Foundation and Contributors | MIT | [source](https://github.com/dotnet/Silk.NET.git) |
| SkiaSharp | 2.88.9 | Microsoft | MIT | [source](https://github.com/mono/SkiaSharp) |
| SkiaSharp.NativeAssets.Linux | 2.88.9 | Microsoft | MIT | [source](https://github.com/mono/SkiaSharp) |
| SkiaSharp.NativeAssets.macOS | 2.88.9 | Microsoft | MIT | [source](https://github.com/mono/SkiaSharp) |
| SkiaSharp.NativeAssets.Win32 | 2.88.9 | Microsoft | MIT | [source](https://github.com/mono/SkiaSharp) |
| System.Buffers | 4.5.1 | Microsoft | see original license | [source](https://dot.net/) |
| System.CodeDom | 9.0.7 | Microsoft | MIT | [source](https://github.com/dotnet/runtime) |
| System.Collections.Immutable | 8.0.0 | Microsoft | MIT | [source](https://github.com/dotnet/runtime) |
| System.Globalization | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.IO | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Management | 9.0.7 | Microsoft | MIT | [source](https://github.com/dotnet/runtime) |
| System.Memory | 4.5.5 | Microsoft | see original license | [source](https://dot.net/) |
| System.Memory | 4.5.4 | Microsoft | see original license | [source](https://dot.net/) |
| System.Numerics.Vectors | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Numerics.Vectors | 4.5.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Numerics.Vectors | 4.4.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Private.Uri | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Reflection | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Reflection.Emit | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Reflection.Emit.ILGeneration | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Reflection.Emit.Lightweight | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Reflection.Metadata | 8.0.0 | Microsoft | MIT | [source](https://github.com/dotnet/runtime) |
| System.Reflection.Primitives | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Resources.ResourceManager | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Runtime | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Runtime.CompilerServices.Unsafe | 6.0.0 | Microsoft | MIT | [source](https://github.com/dotnet/runtime) |
| System.Runtime.Extensions | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Text.Encoding | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Text.Encoding.CodePages | 8.0.0 | Microsoft | MIT | [source](https://github.com/dotnet/runtime) |
| System.Text.Encodings.Web | 8.0.0 | Microsoft | MIT | [source](https://github.com/dotnet/runtime) |
| System.Text.Json | 8.0.0 | Microsoft | MIT | [source](https://github.com/dotnet/runtime) |
| System.Threading.Tasks | 4.3.0 | Microsoft | see original license | [source](https://dot.net/) |
| System.Threading.Tasks.Extensions | 4.5.4 | Microsoft | see original license | [source](https://dot.net/) |

## Eden declared source dependencies

Source: pinned Eden source manifest, at revision `de7e6e01d43e8cf2ec193d74fa053b0d7949955f`. These are **declared build inputs**, not proof of each final binary library's inclusion. Versions and repository identities are reproduced from the project's lock manifest; copyright notices and licenses for actually linked code govern.

| Dependency | Source version/ref | Upstream |
|---|---|---|
| biscuit | v0.19.0 | [source](https://github.com/lioncash/biscuit) |
| boost | 1.92.0 | [source](https://github.com/eden-emulator/ext-boost) |
| boost_headers | boost-1.91.0 | [source](https://github.com/boostorg/headers) |
| catch2 | v3.13.0 | [source](https://github.com/catchorg/Catch2) |
| cpp-jwt | 7f24eb4c32 | [source](https://github.com/arun11299/cpp-jwt) |
| cubeb | fa02160712 | [source](https://github.com/mozilla/cubeb) |
| discord-rpc | 76616d8675 | [source](https://github.com/eden-emulator/discord-rpc) |
| enet | v1.3.18 | [source](https://github.com/lsalzman/enet) |
| ffmpeg | c7b5f1537d | [source](https://github.com/FFmpeg/FFmpeg) |
| ffmpeg-ci | 9.0.2-1790726865-946fcce07b | [source](https://github.com/crueter-ci/FFmpeg) |
| fmt | 12.1.0 | [source](https://github.com/fmtlib/fmt) |
| frozen | 61dce5ae18 | [source](https://github.com/serge-sans-paille/frozen) |
| gamemode | ce6fe122f3 | [source](https://github.com/FeralInteractive/gamemode) |
| httplib | v0.46.0 | [source](https://github.com/yhirose/cpp-httplib) |
| lagoon | 1.0.0 | [source](https://github.com/loongson-community/lagoon) |
| libadrenotools | 8ba23b42d7 | [source](https://github.com/eden-emulator/libadrenotools) |
| libusb | v1.0.29 | [source](https://github.com/libusb/libusb) |
| linkernsbypass | aa3975893d | [source](https://github.com/bylaws/liblinkernsbypass) |
| llvm-mingw | 20250828 | [source](https://github.com/eden-emu/llvm-mingw) |
| lz4 | ebb370ca83 | [source](https://github.com/lz4/lz4) |
| moltenvk | v1.4.1-ryujinx | [source](https://github.com/V380-Ori/Ryujinx.MoltenVK) |
| nlohmann | v3.12.0 | [source](https://github.com/nlohmann/json) |
| oaknut | v2.0.3 | [source](https://github.com/eden-emulator/oaknut) |
| openssl | openssl-3.6.2 | [source](https://github.com/openssl/openssl) |
| openssl-ci | 4.0.1-1788234794-b64f68a94e | [source](https://github.com/crueter-ci/OpenSSL) |
| openssl-cmake | 3.6.2 | [source](https://github.com/jimmy-park/openssl-cmake) |
| opus | a3f0ec02b3 | [source](https://github.com/xiph/opus) |
| quazip | 2e95c9001b | [source](https://github.com/stachenov/quazip) |
| reshade | v6.8.0 | [source](https://github.com/crosire/reshade) |
| sdl3 | release-3.4.8 | [source](https://github.com/libsdl-org/SDL) |
| sdl3-ci | 3.4.14-1788231389-147a8ee32d | [source](https://github.com/crueter-ci/SDL3) |
| simpleini | v4.25 | [source](https://github.com/brofield/simpleini) |
| sirit | v1.0.5 | [source](https://github.com/eden-emulator/sirit) |
| sirit-ci | v1.0.7 | [source](https://github.com/eden-emulator/sirit) |
| spirv-headers | vulkan-sdk-1.4.341.0 | [source](https://github.com/KhronosGroup/SPIRV-Headers) |
| tzdb | 230326 | [source](https://github.com/eden-emu/tzdb_to_nx) |
| vulkan-headers | v1.4.345 | [source](https://github.com/KhronosGroup/Vulkan-Headers) |
| vulkan-memory-allocator | v3.3.0 | [source](https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator) |
| vulkan-utility-libraries | v1.4.345 | [source](https://github.com/KhronosGroup/Vulkan-Utility-Libraries) |
| vulkan-validation-layers | vulkan-sdk-%NUMERIC_VERSION% | [source](https://github.com/KhronosGroup/Vulkan-ValidationLayers) |
| xbyak | v7.40.1 | [source](https://github.com/herumi/xbyak) |
| zbic | 11b08f2712264bbed731545085cbd9702096ceb7 | [source](https://github.com/kinnay/zbic) |
| zlib | v1.3.2 | [source](https://github.com/madler/zlib) |
| zstd | b8d6101fba | [source](https://github.com/facebook/zstd) |

## Citron source dependency families

The pinned Citron adapter uses Citron Neo `598b700884c7cd3bee0a25ce30d0cab066117c5b`. Its reviewed `fetch_dependencies.py` lists these optional/selected upstream dependency families: fmt, lz4, nlohmann_json, ZLIB, LibArchive, zstd, unordered_dense, simpleini, xbyak, Vulkan-Headers, Vulkan-Utility-Libraries, VulkanMemoryAllocator, SPIRV-Headers, enet, opus, SDL2, tzdb_to_nx, sirit, ffmpeg_src, and ffnvcodec. Preserve the corresponding exact source commits, original README/LICENSES, SPDX per-file notices, and documented modifications in the eventual Citron corresponding-source archive. Additional dynamically or statically linked components must be inventoried from the actual stage.

## Other named contributors and upstream intellectual property

- **OpenTK, Silk.NET, SkiaSharp, HarfBuzzSharp, Avalonia, MicroCom, Tmds.DBus.Protocol, JetBrains.Annotations, Humanizer, Concentus, and other NuGet authors** are credited by their exact package rows above and governed by their original notices.
- **OpenAL Soft** and **FFmpeg** are to be credited in the application's About/Credits view and the public download page. Their exact corresponding source/build recipes have not yet been matched to the packaged binary hashes.
- **libnx, newlib, devkitPro, GCC, deko3d and related homebrew-tool authors** are attributed through original license records in the private authored-fixture source; release recipients should receive those notices only where their software or derivatives actually ship.
- **User-supplied original branding** is not under the blanket MIT grant. Nintendo and other third-party marks belong to their respective owners.

## Compliance status and required original files

- Kenji and Canary: keep original MIT terms, per-file copyright, historical Ryujinx notices, LibHac/MIT/ISC/BSD terms, and shipped dependency notices.
- Eden and Citron: **GPL-3.0-or-later combined native worker implementations**. Provide the complete corresponding source for the exact distributed worker revisions, including NX modifications/overlays, build scripts, applicable covered libraries, and original license/credit text, via an accessible public source download. **Do not substitute only the unmodified upstream repositories**.
- Native decoder and audio libs: confirm exact FFmpeg 6.1.2-build4, OpenAL Soft 1.24.3, SDL native payload versions, actual licenses/codec selections, corresponding source plus modifications and build configuration, and LGPL relinking rights if applicable.
- Frontend and runtime: preserve the actual component notices, license texts, and font/icon rights. Existing resolved dependency records are useful **evidence**, not sufficient attribution by themselves.
- MIT API archive: its top-level `LICENSE` refers to `THIRD-PARTY-NOTICES.md`, but that file was excluded from the standalone ZIP. Correct its standalone packaging / obtain final source-archive compliance before publication. A notice solely on this website does not retroactively modify the ZIP.
- No proprietary emulator or Nintendo rights are granted by this inventory. Keep the complete private NX Infinity repository private; publish only the actual corresponding source of GPL-covered binaries and other legally required portions, subject to a verified source-file boundary.

Further developer information: [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html), [FFmpeg legal checklist](https://ffmpeg.org/legal.html), [SDL license](https://www.libsdl.org/license.php).

