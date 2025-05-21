# AOE HWID Tool

A no-frills command-line utility for spoofing various hardware identifiers on Windows. Portions of this implementation draw inspiration from @LockBlock-dev.

---

## 📋 Supported Systems

- **Windows 11** (10.0.22621 Build 22621) ✅  
- **Windows 10** (22H2 Build 19045.2965) ✅  

> ⚠️ _This project is a work in progress—while many routines function reliably, the spoofer is not yet foolproof. Feedback and contributions are welcome!_

**Download** - [Click here](https://github.com/notbruto/AOE_HWID_tool/releases/tag/v.1%2B)

---

## ⚡ Core Features

### 1. Disk Identifier Spoofing  
**Added:** May 18, 2023  
- Scans the registry for SCSI bus and port entries  
- Identifies disk-type devices  
- Generates randomized vendor/product IDs and serial numbers  
- Writes new values back into the registry  

### 2. GUID Regeneration  
**Added:** May 18, 2023  
- Creates fresh GUIDs for all major system keys  
- Updates `HwProfileGuid`, `MachineGuid` and `MachineId`  
- Assigns a randomized BIOS release date  

### 3. Computer Name Override  
**Added:** May 18, 2023  
- Reads the current PC name from registry  
- Crafts a new random hostname  
- Updates `ComputerName`, `ActiveComputerName`, `Hostname` and network-related entries  

### 4. MAC Address Spoofing  
**Added:** May 19, 2023  
- Enumerates network adapters via registry  
- Generates a random, valid MAC address  
- Applies the new MAC in registry and toggles the adapter to commit changes  

### 5. Game Cache Cleanup  
**Added:** May 19, 2023  
- **Ubisoft:** Purges local cache files  
- **Valorant (Riot):** Clears game cache  

### 6. Windows Installation ID Forge  
**Added:** May 26, 2023  
- Reads existing `MachineGuid`  
- Generates and applies a brand-new GUID  
- Logs before/after values for audit  

### 7. EFI Bootloader Spoofing  
**Added:** May 26, 2023  
- Opens EFI variable store in registry  
- Generates a fresh EFI variable ID  
- Updates registry entry  

### 8. SMBIOS Serial Randomizer  
**Added:** May 26, 2023  
- Targets `SystemSerialNumber` in SMBIOS data  
- Produces a new random serial number  
- Writes change to registry  

### 9. System Information Dump  
**Added:** May 27, 2023  
- Retrieves and displays comprehensive system details  

### 10. Registry Integrity Checker  
**Added:** June 7, 2023  
- Defines a checklist of critical registry paths  
- Reports any missing entries or confirms completeness  

### 11. Change Logging  
**Added:** June 10, 2023 (Experimental)  
- Records every registry change in a timestamped `.txt` file  

### 12. Registry Backup Utility  
**Added:** June 13, 2023 (Experimental)  
- Exports selected keys into a `.reg` backup  

### 13. Product ID Spoofer  
**Added:** June 14, 2023 (Experimental)  
- Targets `ProductId` under  
  `SOFTWARE\Microsoft\Windows NT\CurrentVersion`  
- Generates a 20-character random product ID  
- Writes new value back to registry  

### 14. Display Settings Randomizer  
**Added:** June 15, 2023 (Experimental)  
- Modifies MRU display entries (`MRU0…MRU4`)  
- Assigns fresh display IDs via registry  

### 15. SecHex Cleanup Suite  
**Added:** June 28, 2023 (Testing)  
- Flushes DNS cache  
- Cleans temporary files, Windows logs, Chrome cookies, recent docs  
- Resets TCP connections  
- Terminates anti-cheat services (Fortnite, Valorant, FiveM, etc.)  
- Unlinks Xbox and Discord integrations  

---

## 🎯 Development Milestones

| Stars Achieved | Feature                                           | Status |
|---------------:|---------------------------------------------------|:------:|
| 5 ★            | EFI Spoofing                                       | ✅     |
| 10 ★           | SMBIOS Spoofing                                    | ✅     |
| 20 ★           | Full GUI & Spoofer Engine                         | ✅     |
| 50 ★           | GUI Enhancements                                   | ✅     |
| 100 ★          | Major Code Refactor & Regular Updates              | ✅     |
| 500 ★          | Kernel-Level Driver Integration                    | ❌     |

> **Progress:** ▰▰▰▰▰▰▰▰▰▰▱▱▱ (75% complete)

_Currently collaborating with @toto and @Starcharms on the kernel-mode driver for deep-level HWID spoofing on both Windows 10 and 11._

---

## 🔧 Usage

1. Download AOE tool
2. Execute under UAC
3. Spoof your system!
