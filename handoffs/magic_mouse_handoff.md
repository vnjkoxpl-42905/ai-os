# Session Handoff: Magic Mouse 2 Configuration (Revised)

**Goal:** Configure Apple Magic Mouse 2 on Windows 11 with maximum functionality for $0, maintaining Absolute Security (no Test Signing, no disabling HVCI, no disabling Secure Boot).

## Current State
- **Pre-Install Verifications Complete:** 
  1. `AppleWirelessMouse.cat` signature verified as Valid.
  2. Complete hardware/instance IDs (including Touchpad/Vendor-defined nodes) mapped.
  3. Existing filter configuration backed up to `C:\Users\Joshu\Desktop\MagicMouse_FilterBackup.txt`.
- **Driver Readiness:** The pristine Apple Boot Camp driver (via Brigadier) is waiting at `C:\Users\Joshu\Desktop\PristineMagicMouseDriver`.

## Instructions for Next Agent
1. **Driver Installation:** Instruct the user to install the driver. *Do not assume it works on a success message.* After installation/reconnect, you must explicitly query the device nodes to verify that `applewirelessmouse.sys` has successfully attached to the Magic Mouse device node. Treat it as a lower filter unless inspection proves otherwise.
2. **Capability Testing (STOP HERE):** Before doing anything else, run a comprehensive test with the user:
   - Pointer, Left/Right click, Vertical/Horizontal scroll, Smoothness.
   - Sleep/wake, Bluetooth reconnect, and Windows reboot stability.
   - **Crucial:** Inspect what Windows actually receives (standard wheel events vs. Raw HID). Do NOT assume the driver consumes all touch data—measure it.
3. **Present Results:** Show the user the capability matrix and wait for approval.
4. **AutoHotkey Augmentation (Only after testing):** 
   - Map `Alt` + horizontal scroll to Virtual Desktops (if HWHEEL exists).
   - Use a modifier+click for Middle Click (do not rely on L+R simultaneous click due to the unified surface mechanics).
   - Treat `Ctrl`+vertical-scroll as app zoom.
5. **Natural Scrolling:** Target the exact Magic Mouse HID node, back up its parameters, and test `FlipFlopWheel` / `FlipFlopHScroll` individually. Do not apply globally.
