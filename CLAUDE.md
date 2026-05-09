# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a binary distribution repository — it contains no source code. The repo holds a single Android APK (`VideoChat's.apk` and `VideoChats`, which are the same file) distributed to users.

- **APK package**: `com.android.app`
- **Built with**: Kotlin (confirmed by bundled Kotlin metadata)
- **APK size**: ~6.1 MB, signed with APK Signing Block

## Repository Contents

| File | Description |
|------|-------------|
| `VideoChat\`s.apk` | Signed Android APK (primary artifact) |
| `VideoChats` | Identical copy of the APK without backtick in filename |
| `README.md` | Minimal readme (`# he`) |

## Working with the APK

Since only the compiled binary is present, there are no build, lint, or test commands available in this repository.

To inspect APK contents:
```bash
# List files inside the APK
unzip -l "VideoChat\`s.apk"

# Extract and read the binary manifest
unzip -p "VideoChat\`s.apk" AndroidManifest.xml | strings

# Decompile for analysis (requires apktool installed)
apktool d "VideoChat\`s.apk" -o apk_decoded/
```

## Key Constraints

- There is no source code to edit, build, or test in this repository.
- Any modifications to the APK require the original source project (not present here).
- The two APK files (`VideoChat\`s.apk` and `VideoChats`) should be kept in sync — they are the same artifact with different filenames.
