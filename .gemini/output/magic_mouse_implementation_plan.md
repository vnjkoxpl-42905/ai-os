# Magic Mouse 2 Setup Plan (100% Free & Secure)

We are taking a safe, staged approach to maximize your Apple Magic Mouse 2 (VID `05AC`, PID `0269`) capabilities on Windows 11 without spending any money and without compromising Windows security. 

## User Review Required
> [!IMPORTANT]
> The implementation plan entirely avoids experimental kernel drivers that require disabling **Secure Boot**, **Test Signing**, or **Memory Integrity (HVCI)**. Some GitHub projects (like `chrischip/magic-mouse-windows` or `magicmouse-ptp`) claim to offer richer native gestures, but our research confirms they currently force you to disable Memory Integrity and/or enable Test Signing. We are adhering to your rule to reject these approaches by default.

## Verification / Context
- **Hardware ID Confirmed:** Your mouse reports as `HID\VID_05AC&PID_0269`.
- **Target Approach:** We will extract the digitally signed Apple Boot Camp driver to restore baseline multi-touch (Stage 2) and then map any emitted raw inputs to gestures using free user-space utilities (Stage 4/5).

---

## Proposed Changes

We will execute the 5 stages exactly as requested.

### Stage 1: Hardware Identification (Completed)
- We successfully captured the Instance ID and Hardware ID of the connected mouse: `VID_05AC&PID_0269`.

### Stage 2: Safely Extract & Install Official Apple Driver
- Create a Windows System Restore point so all changes can be immediately reverted if needed.
- Use the open-source tool `Brigadier` to download *only* the specific Apple Boot Camp driver package (`Macmini8,1` profile is confirmed to include modern Bluetooth 5 / Magic Mouse 2 drivers).
- Extract **only** `AppleWirelessMouse64.exe` (or the raw `.inf` files) from the payload.
- Install the driver natively into Windows 11.

### Stage 3: Capability Matrix Testing
Once the driver is active, I will pause and ask you to test the mouse. We need to measure exactly what the official driver emits. We will test:
- [ ] Smooth Vertical Scrolling
- [ ] Horizontal Scrolling
- [ ] Middle Click (e.g., two-finger tap)
- [ ] Swipe Gestures (if any register)
- [ ] Battery Reporting

### Stage 4 & Stage 5: Free User-Space Augmentation
- Based on the matrix, we will install **AutoHotkey (AHK)** or a similar user-space hook (like Magic Mouse Scroll utilities that don't replace the kernel driver). 
- If the Apple driver emits standard `WM_MOUSEHWHEEL` events for horizontal swipes, we can map them to custom Windows actions (e.g., Task View, Virtual Desktop switching).
- **Rule Check:** This stage ensures $0 cost while keeping all Windows driver-signature enforcement enabled.

---

## Verification Plan

### Manual Verification
1. I will run the Brigadier command, extract the driver, and install it via `pnputil` or the `.exe`.
2. I will ask you to reconnect the Bluetooth mouse.
3. You will manually confirm if vertical/horizontal scrolling works natively.
4. Based on your feedback, I will generate the exact AHK scripts to bridge any missing gaps (like middle-click or swipe-to-screenshot) that the raw driver supports.
