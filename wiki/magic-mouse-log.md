# Apple Magic Mouse 2 Execution Log

Date: 2026-09-18
Target: Apple Magic Mouse 2 on Windows 11 (Dell Laptop)
Objective: Maximum functionality for $0 without security compromises.

---

## Phase 1.1 — Baseline State (Pre-Installation)

### Hardware Identification
- **Friendly Name:** Magic Mouse 2
- **Device Class:** Bluetooth
- **Bluetooth Instance ID:** `BTHENUM\DEV_C40B31171FAD\7&1B3B267E&0&BLUETOOTHDEVICE_C40B31171FAD`
- **Bluetooth Hardware ID:** `BTHENUM\Dev_C40B31171FAD`
- **Parent Controller:** `BTH\MS_BTHBRB\6&2b760b08&0&1`

### Active Bluetooth HID Stack
- **Bluetooth HID Device Node:**
  - **Instance ID:** `BTHENUM\{00001124-0000-1000-8000-00805F9B34FB}_VID&0001004C_PID&0269\7&1B3B267E&0&C40B31171FAD_C00000000`
  - **Hardware IDs:**
    - `BTHENUM\{00001124-0000-1000-8000-00805f9b34fb}_VID&0001004c_PID&0269`
    - `BTHENUM\{00001124-0000-1000-8000-00805f9b34fb}_LOCALMFG&005d`
  - **Driver Provider:** Microsoft
  - **Driver Version:** 10.0.26100.8737
  - **Driver INF:** `hidbth.inf`
  - **Service:** `HidBth`
  - **LowerFilters:** (none)
  - **UpperFilters:** (none)

### Active Child HID Devices
1. **Mouse Node:**
   - **Instance ID:** `HID\{00001124-0000-1000-8000-00805f9b34fb}_VID&0001004c_PID&0269&Col01\8&2522c251&0&0000`
   - **Friendly Name:** HID-compliant mouse
   - **Class:** Mouse
   - **Driver Provider:** Microsoft
   - **Driver Version:** 10.0.26100.1150 (`msmouse.inf`)
   - **Service:** `mouhid`
2. **Vendor-Defined Node:**
   - **Instance ID:** `HID\{00001124-0000-1000-8000-00805f9b34fb}_VID&0001004c_PID&0269&Col02\8&2522c251&0&0001`
   - **Friendly Name:** HID-compliant vendor-defined device
   - **Class:** HIDClass

### Rollback File
- Backed up filter configuration saved to: `C:\Users\Joshu\Desktop\MagicMouse_FilterBackup.txt`

---

## Phase 1.2 — Apple INF Technical Analysis

- **Source File:** `C:\Users\Joshu\Desktop\PristineMagicMouseDriver\AppleWirelessMouse.inf`
- **Driver Version:** `06/21/2018, 6.1.7000.0`
- **Provider:** Apple Inc.
- **Catalog File:** `applewirelessmouse.cat` (Digitally signed by Microsoft Windows Hardware Compatibility Publisher, status: Valid)
- **Architecture:** `NTamd64` (x64)
- **Class:** `HIDClass` (`{745a17a0-74d3-11d0-b6fe-00a0c90f57da}`)
- **Matching Hardware IDs in INF:**
  - `BTHENUM\{00001124-0000-1000-8000-00805f9b34fb}_VID&000205ac_PID&030d` (Magic Mouse 1)
  - `BTHENUM\{00001124-0000-1000-8000-00805f9b34fb}_VID&000205ac_PID&0310` (Magic Mouse 1 alt)
  - `BTHENUM\{00001124-0000-1000-8000-00805f9b34fb}_VID&0001004c_PID&0269` (**Magic Mouse 2 — exact match for active Bluetooth HID Device**)
- **Driver Role:** **LowerFilter** (`HKR,,"LowerFilters",0x00010000,"applewirelessmouse"`) underneath `hidbth.inf`
- **Service Created:** `applewirelessmouse`
  - **Service Binary:** `%SystemRoot%\System32\drivers\applewirelessmouse.sys`
  - **Service Type:** `SERVICE_KERNEL_DRIVER` (0x1)
  - **Start Type:** `SERVICE_DEMAND_START` (0x3)
