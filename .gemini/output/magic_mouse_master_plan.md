# Magic Mouse 2 on Windows 11: Free & Secure Master Plan (Revised)

## 1. Executive Summary & Security Directives
**Target:** Maximum Apple Magic Mouse 2 functionality on Windows 11 for exactly $0.
**Absolute Security Constraints:** Do NOT disable Secure Boot, Memory Integrity (HVCI), or driver-signature enforcement. Do NOT enable Test Signing. Do NOT use paid Magic Utilities.

The required Apple Boot Camp driver has been safely obtained via Brigadier and placed at `C:\Users\Joshu\Desktop\PristineMagicMouseDriver`.

---

## 2. Pre-Installation Verification (Completed)
Before proceeding, we ran verification tests on the system:
1. **Signatures:** The `AppleWirelessMouse.cat` signature is confirmed **Valid** (Signer: Microsoft Windows Hardware Compatibility Publisher).
2. **Hardware & Instance IDs:** The device `VID_05AC&PID_0269` enumerates multiple HID nodes (including generic mouse, touchpad `UP:000D_U:0005`, and vendor-defined nodes). 
3. **Backup:** Existing Device/Filter configurations have been backed up to `C:\Users\Joshu\Desktop\MagicMouse_FilterBackup.txt`.

---

## 3. Safe Driver Installation
We will install **only** the `AppleWirelessMouse.inf` driver. 

*Crucial Verification:* Simply right-clicking "Install" is not enough. We must verify that `applewirelessmouse.sys` actually attaches to the correct Magic Mouse device node. Until confirmed otherwise by direct inspection, we treat this driver as a **lower filter** in the HID stack.

---

## 4. Capability Matrix & Raw Event Testing
Before any user-space software (like AutoHotkey) is introduced, we must perform a strict capability baseline test. We will test and document:
- [ ] Pointer movement
- [ ] Left click & Right click
- [ ] Vertical & Horizontal scrolling (including scroll smoothness)
- [ ] Natural-direction behavior
- [ ] Any distinct one-finger/two-finger behaviors
- [ ] Middle-click possibilities (if mechanically possible without chords)
- [ ] Battery reporting
- [ ] Bluetooth off/on reconnect, Sleep/wake, and Windows reboot reliability

**Raw Input Inspection:** We will measure exactly what Windows receives (e.g., standard button events, `WM_MOUSEWHEEL`, `WM_MOUSEHWHEEL`, or raw HID data). We will **not** assume the Apple driver consumes all raw touch data; we will measure what remains visible to user mode.

---

## 5. Free User-Space Augmentation (Post-Test Only)
Only after the capability test proves which events exist will we design AutoHotkey v2 augmentations.
- **Virtual Desktops:** If horizontal wheel events are confirmed, map Horizontal scroll + Alt to Ctrl+Win+Left/Right.
- **Middle Click:** Because the unified surface mechanically restricts simultaneous physical clicks, we will use a reliable modifier+click mapping instead of simultaneous L+R clicks.
- **Zoom:** Ctrl+vertical-scroll will be treated as application zoom where supported.

---

## 6. Natural Scrolling targeting
We will identify the *exact* Magic Mouse HID scrolling node first, back up its `Device Parameters`, and test `FlipFlopWheel` and `FlipFlopHScroll` individually. We will not blindly modify these values across every mouse/HID device on the system.
