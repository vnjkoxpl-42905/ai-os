# Session Handoff: Magic Mouse 2 Configuration

**Goal:** Configure Apple Magic Mouse 2 on Windows 11 with maximum functionality for $0, without compromising Secure Boot, Driver Signature Enforcement, or Memory Integrity.

## Current State
- **Hardware Identifiers:** Magic Mouse 2 is paired via Bluetooth (`VID_05AC&PID_0269`).
- **The Core Problem:** Generic Windows HID drivers ignore Apple's multi-touch surface data. Standalone extracted `.inf` drivers from GitHub break catalog hashes due to CRLF/LF conversion, leading to security warnings unless test signing is enabled (which violates the user's constraints).
- **The Solution:** We are using `timsutton/brigadier` in the background to download the pristine Boot Camp 6.x package (`Macmini8,1`) directly from Apple's CDN. We are extracting the signed `AppleWirelessMouse` driver from the `.pkg` and placing it on the desktop for the user to install cleanly.
- **Background Task:** A PowerShell script is currently running (Task 48) to download the ~1GB package, extract the mouse driver to `C:\Users\Joshu\Desktop\PristineMagicMouseDriver`, and delete the rest of the Bloatware.

## Next Steps for the Agent / User
1. **Verify Download:** Check if `C:\Users\Joshu\Desktop\PristineMagicMouseDriver` has been created and populated with the `.inf`, `.cat`, and `.sys` files.
2. **Install Driver:** The user needs to install the `.inf` file from the Desktop folder (Right-click -> Install, or use `pnputil`). This will grant smooth vertical and horizontal scrolling.
3. **Run Capability Matrix:** Ask the user to confirm vertical and horizontal scrolling are active natively.
4. **Deploy AHK Script:** Provide the user with the AutoHotkey v2 script documented in `magic_mouse_master_plan.md` to emulate Middle-Click, Virtual Desktop switching (`Alt` + Horizontal Swipe), and Task View shortcuts.
5. **Set Natural Scrolling (Optional):** Guide the user to flip `FlipFlopWheel` in the Registry if they prefer macOS-style scroll inversion.

## Key Directives
- **Do not** attempt to install `chrischip/magic-mouse-windows` or `magicmouse-ptp`. They require Test Signing and disabling HVCI. 
- **Do not** use Magic Utilities, as it becomes paid software after 28 days.
