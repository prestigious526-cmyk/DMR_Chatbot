# Secure HHPC — DMR Handheld Radio (VHF): Technical Manual

> **Note:** Secure HHPC is also referred to as DMR HANDHELD (VHF) throughout this document.

---

# Part 1 — Technical Specifications

## 1.1 Introduction

The Secure HHPC is a handheld radio set for secure voice communication in the VHF band with short data messaging capability. It is a digital protocol radio with a built-in encryption card for high-end secrecy requirements.

### Operating Modes

| Mode | Channel Spacing |
|---|---|
| Secure DMR (digital) | 12.5 kHz |
| Analog FM (admin mode only) | 25 kHz |

### Frequency Range

- 136 MHz to 174 MHz

### Key Operational Characteristics

- Preset channels and functions selectable via rotary switches
- Radio functions configurable via alphanumeric front-panel keypad and Customer Programming Software (CPS)
- Two power output levels (high and low) selectable via front panel or CPS, channel-by-channel
- Line-of-sight (LOS) communication in clear and secure mode
- Battery operated
- Compatible with legacy radio in clear FM wideband mode
- Complies with ETSI standard for DMR protocol
- Analog communication available in password-protected admin mode

### Supported Features

- Dual mode operation (Analog and Digital DMR)
- Analog 25 kHz wideband
- Built-in graded encryption
- DMR Individual Call
- DMR Group Call
- DMR Broadcast Call
- SMS (short data messaging)
- DMR Radio Check
- DMR Radio Enable / Disable
- DMR Call Alert
- Caller ID Display
- DMR Late Entry
- Emergency Button (SOS)
- Battery Strength Indicator
- Man Down detection

---

## 1.2 Equipment and Accessories

### Table 1-1 — List of Equipment and Accessories

| Sl. No. | Description | BEL Part No. |
|---|---|---|
| 1 | SECURE HHPC | 171000580163 |
| 2 | CHARGER WITH ADAPTER (DMR) | 171000604122 |
| 3 | PROG Cable H/H DMR | 450671190362 |
| 4 | CD PROGRAMMING S/W (DMR HH) | 458671820105 |
| 5 | BATTERY ASSY DMR HH | 171000602667 |
| 6 | VOX (DMR HH) | 171000611979 |

---

## 1.3 Dimensions and Weight

### Table 1-2 — Physical Dimensions

| Description | Height (mm) | Width (mm) | Depth (mm) | Weight |
|---|---|---|---|---|
| SECURE HHPC | 140 ± 5 | 60 ± 2 | 48 ± 3 | 480 g (max) |

---

## 1.4 General Characteristics

### 1.4.1 Modes of Operation

- Conventional analog: FM Half Duplex (Clear Voice), wideband 25 kHz channel spacing
- Digital TDMA: Digital Clear Voice; Digital Secure Voice and Data (Custom mode)
- Digital Vocoder: AMBE+2
- Modulation: Analog — FM (25 kHz); Digital — 4FSK

### 1.4.2 Frequency Characteristics

| Parameter | Value |
|---|---|
| Frequency range | 136–174 MHz |
| Channel spacing — DMR mode | 12.5 kHz |
| Channel spacing — Analog mode | 25 kHz |
| Channel capacity | ≥ 255 |
| Antenna impedance / type | 50 Ω / helical |
| Supply voltage (nominal) | 8.0 V DC |
| Permissible supply range | 6.5 V to 8.6 V |

---

## 1.5 Radio Features

### 1.5.1 Remote Monitor

Allows a remote user to activate the microphone and transmitter of a target (misplaced or lost) HHPC for a period of time, to assist in accessing communication on the lost handset.

### 1.5.2 Late Entry

Supports late entry call in DMR mode.

### 1.5.3 Remote Enable / Disable

Allows stopping inappropriate use of an HHPC or preventing a stolen HHPC from functioning, remotely.

### 1.5.4 Emergency Call

Short-duration high-power transmission for sending emergency notification to personnel at site.

### 1.5.5 Call Types

Individual, group, and broadcast call facility.

### 1.5.6 Data Messaging (SMS)

SMS texting facility in DMR mode.

### 1.5.7 Encryption

Provision for SAG integration graded algorithm / encryption module for supplementary encryption.

### 1.5.8 Lone Worker Mode

Automatic periodic check on personnel working alone at site.

### 1.5.9 Man-Down Feature

Special motion sensors detect man-down positions of an individual.

### 1.5.10 GPS Tracker

Inbuilt GPS tracker with 10 m accuracy. Supports requesting and responding to GPS location from another HHPC.

### 1.5.11 MMI Display

LCD with standard keypad. Displays GPS coordinates, battery strength indicator, Caller ID, channel numbers.

### 1.5.12 Scanning — Priority / Emergency

Automatically scans each channel in turn and alerts the user on the active channel.

### 1.5.13 Fill Gun Interface

Receives secure key data from a Fill Gun when connected and when the Fill Gun's LOAD key is pressed. Password protected.

### 1.5.14 PC Interface (CPS)

Receives AES key data and preset frequency table from PC via COM port loaded with CPS software.

### 1.5.15 VSWR Protection

RF power output maintained per specification after subjecting the radio set to open-circuit at the antenna port for short PTT pressing.

### 1.5.16 Reverse Polarity Protection

No permanent damage to the radio on reversal of power supply polarity.

### 1.5.17 Backlit Keypad Illumination

Backlit illumination available on the keypad.

### 1.5.18 Keypad Locking

Keypad locking facility available.

### 1.5.19 DCDM Mode

Two-slot operation on a single channel (Dual Capacity Direct Mode).

### 1.5.20 Digital Sensitivity

Minimum −117 dBm for 5% BER.

### 1.5.21 Remote Kill

Remotely kills another HHPC. Involves algorithm erase and key erase.

### 1.5.22 Battery Life

- Custom digital mode: 11 hours
- Analog mode: 9 hours
- Duty cycle: 1:1:18 ratio (Tx : Rx : Standby)

### 1.5.23 Spurious Response Rejection

60 dB or better.

### 1.5.24 Interoperability

Interoperable with existing IAF HHPC in clear FM wideband mode.

### 1.5.25 VOX (Voice Activation)

Transmit mode operable by voice in VOX mode.

---

# Part 2 — Technical Specifications (Detailed)

## 2.1.1 Analog Mode Specifications

### Receiver Parameters — Analog Mode

| Parameter | Specification |
|---|---|
| Sensitivity (SINAD) | Min 12 dB at RF input level of −115 dBm |
| Audio output power | Min 1 W at full volume |
| Audio distortion | Less than 5% |
| Audio response | +1 dB, −3 dB |
| Squelch sensitivity | Opens at min RF input of −117 dBm |
| Rx frequency stability | ±1 ppm |

### Transmitter Parameters — Analog Mode

| Parameter | Specification |
|---|---|
| RF power output — High Power | 5 W ± 1 dB |
| RF power output — Low Power | 1 W ± 1 dB |
| Frequency stability | Within ±1 ppm |
| Audio deviation (25 kHz) | 5 kHz ± 1.5 kHz at 10 mV input at 1000 Hz |
| Audio distortion | Less than 5% |
| Transmit current | ≤ 2.5 A |
| Adjacent channel power | −60 dB or better |

## 2.1.2 Digital Clear Mode Specifications

### Receiver Parameters — Digital Clear Mode

| Parameter | Specification |
|---|---|
| Audio output power | Min 1 W at full volume |

### Transmitter Parameters — Digital Clear Mode

| Parameter | Specification |
|---|---|
| RF power output — High Power | 5 W ± 1 dB |
| RF power output — Low Power | 1 W ± 1 dB |

---

# Part 3 — Hardware Interface Components

## System Overview

The Secure HHPC has front, side, and top panel interfaces for radio operation, transmission, emergency alert, configuration, and menu control.

---

## Component: VHF Antenna

- **Aliases:** antenna, RF antenna, VHF whip antenna
- **Location:** Top of the radio
- **Function:** Transmits and receives VHF radio frequency signals
- **Fault relevance:** loose antenna, damaged antenna, weak signal, reduced range, no reception, poor transmission

## Component: Channel Selector Knob

- **Aliases:** channel knob, selector dial, channel switch
- **Location:** Top panel
- **Function:** Selects programmed radio channels
- **Fault relevance:** channel not changing, skipped channels, wrong channel selection, stiff rotation, selector failure

## Component: ON/OFF and Volume Control Knob

- **Aliases:** power knob, volume knob, power/volume control
- **Location:** Top panel
- **Function:** Turns the radio ON or OFF and adjusts speaker volume
- **Fault relevance:** radio not powering on, unexpected shutdown, no audio, low volume, volume not adjustable

## Component: SOS Button

- **Aliases:** emergency button, distress button, alarm button
- **Location:** Top front section
- **Function:** Triggers emergency alert or emergency transmission
- **Fault relevance:** SOS not responding, emergency alert not sent, accidental activation, button failure

## Component: TX ON LED

- **Aliases:** transmit LED, TX indicator, transmit light
- **Location:** Front upper section
- **Function:** Indicates that the radio is transmitting
- **Fault relevance:** LED not glowing during transmit, LED always ON, incorrect transmit indication

## Component: Programming Connector

- **Aliases:** program port, service connector, configuration connector
- **Location:** Side / front interface area
- **Function:** Connects radio for programming, firmware upload, configuration, and diagnostics
- **Fault relevance:** device not detected, failed programming, intermittent connection, connector damage

## Component: PTT Button

- **Aliases:** push-to-talk, transmit button, press-to-talk button
- **Location:** Side panel
- **Function:** Activates transmission while pressed
- **Fault relevance:** no transmit on press, stuck transmit, delayed transmit, button not working

## Component: Side Keys

- **Aliases:** programmable side buttons, function keys, shortcut keys
- **Location:** Side panel below PTT
- **Function:** User-programmable buttons for assigned functions
- **Typical assigned functions:** scan, monitor, alert, power level, shortcut operations
- **Fault relevance:** no response, wrong function, key mapping issue, damaged switch

## Component: Display Screen

- **Aliases:** LCD, display, screen
- **Location:** Front lower section
- **Function:** Shows channel, RX/TX status, menu options, and status messages
- **Fault relevance:** blank screen, flickering, unreadable text, backlight failure

## Component: Keypad

- **Aliases:** numeric keypad, front keys, input keys
- **Location:** Bottom front section
- **Function:** Menu navigation, numeric input, and radio commands
- **Fault relevance:** keys not responding, stuck buttons, incorrect input, keypad wear

---

# Part 4 — System Architecture and Block Diagram

## Major Modules

| Module | BEL Part Number |
|---|---|
| PWA PGMD BB CARD DMR HANDHELD (Baseband Card) | 128380001005 |
| PWA ENCRYPTION (Crypto Card) | 171300826591 |
| PWA POWER AMPLIFIER MODULE (VHF) | 171300837552 |
| DISPLAY TFT SPI | 446071480141 |
| KEYPAD DMR 18 KEYS-II | 471683040235 |

## Transmit Path

1. Clear voice received from mic (internal or external) via Codec.
2. Data processed in required format.
3. Controller checks for presence of encryption module PCB (handshake).
4. If handshake successful: call or message initiated.
5. Custom channel configured only after successful handshake.
6. In **custom encryption mode**: voice/data passed to crypto card for encryption, then to TX up-converter IC, then to Power Amplifier card.
7. In **DMR clear mode**: data passed to encryption module PCB (no encryption performed), then modulated and sent to Power Amplifier card.
8. For **SMS**: data transmitted instead of voice in the same manner.
9. For **analog wideband mode**: user must first enter admin mode; handshake with encryption module PCB must succeed; plain FM in 136–174 MHz range.

## Receive Path

1. Amplified signal received from RF (PA) card.
2. Down-converted to baseband level via down-converter IC.
3. Data passed to DMR processor for audio level conversion (Codec used).
4. In **custom encryption mode**: data decrypted using crypto card before audio output.

---

## Module Descriptions

### Baseband Card

- **Reference:** BD 1713 008 376 49
- Battery mating connector mounted directly on baseband card; receives +7.4 V (nom) from battery.
- Contains DC-DC converters: **U24** converts 7.5 V (nominal) from battery to **5 V** and **3.6 V**.
- Further DC conversions power analog and digital PCB sections.
- Digital section: ARM Cortex-M4 Controller + DMR Processor.
- Provides user interface via keypad and backlit graphic LCD display.
- Hosts detachable encryption module (algorithm for custom encryption).
- Contains interface ICs for GPS and man-down feature.
- Encryption module is required for all communication types.
- In analog wideband mode (25 kHz): encryption module presence verified via I2C handshake.
- In DMR clear mode: data passed to encryption module, but no encryption performed.

#### Controller (MCU)

- Type: 32-bit ARM Cortex-M4 with FPU; includes ARM Cortex-M0 coprocessor
- Flash: 1 MB; SRAM: 136 kB; EEPROM: 16 kB (on-chip)
- Clock: 12.28 MHz; Supply: 3.3 V DC
- Controls all interfaces: keypad input, display output
- Interfaces with crypto card via I2C
- Interfaces with GPS and man-down ICs

#### DMR Processor (DSP)

- Responsible for analog mode and digital protocol implementation
- External clock: 12.28 MHz
- I/O section supply: 3.3 V; Core section supply: 1.2 V
- Complies with ETSI TS 102 361 in DMR mode
- Processes: digital processing, 4-level FSK and baseband filter, vocoder (audio codec ADC/DAC), data scrambling, pre-emphasis/de-emphasis, compressor/expander, DMR protocol

### Power Amplifier (PA) Card

- **Reference:** BD 1713 008 375 52
- **Receive mode (PTT not pressed):** accepts receive signal, performs harmonic filtering, amplifies via LNA, sends to baseband card.
- **Transmit mode (PTT pressed):** amplifies transmit signal from BB card to 5 W (high power) or 1 W (low power).
- **GPS function:** extracts GPS signal from receive signal and sends to baseband card.

### Crypto Card

- **Reference:** Figure 1.8.4
- Provides data encryption and decryption.
- Physically mounted as a detachable module on the baseband module.
- FPGA-based high-performance card.
- Interfaces with baseband module via I2C (data communication) and UART (key and algorithm loading).
- Internal components: SPI Flash, RTC, Schmitt trigger-based RNG circuit.

### LCD Display

- Size: 1.77 inch; Type: TFT, Normally White, transmissive
- Dimensions: 34.0 (W) × 45.83 (H) × 2.65 (D) mm
- Supply voltage (analog min): 2.5 V; Current: 0.9 A

#### LCD Pin Definition

| Pin | Symbol | I/O | Function |
|---|---|---|---|
| 1 | LED+ | P | Backlight anode |
| 2 | LED− | P | Backlight cathode |
| 3 | SPI4W (VCC=4 WIRE) | I | SPI4W='0': 3-line SPI enabled; SPI4W='1': 4-line SPI enabled; if not used, fix at DGND |
| 4 | VCC | P | Power supply |
| 5 | GND | P | Ground |
| 6 | CS | I | Chip enable (CSX) |
| 7 | RST | I | Reset signal (RESX) |
| 8 | SDA | I/O | Serial input/output in serial interface mode |
| 9 | SCL | I | Serial clock in serial interface mode |
| 10 | D/C | I | Data / command selection (D/CX) |

### Keypad

- 18-key keypad
- Connected to baseband card via 14-pin connector
- Matrix: 3 × 6
- Backlit; backlight controlled by the controller
- Used for entering user data

---

# Part 5 — Accessories

## Mother Fill Gun (MFG) — BEL P/N 171000649130

Stores and loads keys to Child Fill Guns. Child Fill Guns in turn load keys to secure communication equipment.

## Child Fill Gun (CFG) — BEL P/N 171000649227

Receives keys from MFG; loads keys to the equipment. Draws power from the equipment.

## Key Gen Equipment (KGE) — BEL P/N 171000649324

Generates keys using PC. Essential for the key loading procedure.

## Algo Loading Device (ALD) — BEL P/N 171000649421

Loads algorithms to the equipment. Draws power from the equipment.

## Carrying Case (DMR HH) — BEL P/N 171000612076

Transports the equipment and accessories. Moulded plastic case with cross-linked polythene moulding.

---

# Part 6 — Inspection, Maintenance, and Test Procedures

## 6.1 General Precautions

- DMR HHPC is modular in construction; connectors and sockets are polarized — no interchange possible.
- Disconnected wires must be tagged and marked for identification during reassembly.
- Modules must be seated on rivet spacers/guides before tightening.
- For test instruments: set higher measuring range first to protect from overload.

## 6.2 Preventive Maintenance

- Equipment is gasket-sealed; dust ingress is minimized.
- If kept open or unattended for prolonged periods: clean with low-pressure vacuum cleaner or soft dry cloth.
- Switch contacts: clean with Isopropyl Alcohol.
- Cable ends: arrange to prevent short circuits and strain on wires and lugs.
- Corrosion: clean surface and touch up with Zinc chromate primer.
- Do not use oils, paints, or varnish near relays and switches.

## 6.3 Periodic Maintenance Schedule

### Daily

- Verify equipment and accessories are complete.
- Check for physical damage; ensure all controls move smoothly.
- Ensure all fasteners are tight and dust-free.
- Confirm display window is not broken.

### Weekly

- Inspect canvas items for mildew and tears.

### Monthly

- Check painted surface finish.
- Inspect canvas accessories for tears and damage.
- Press the **iBITE** button (in Power On condition) to confirm healthy equipment status.

## 6.4 Maintenance During Storage

- If stored for more than 3–4 months: take out, clean, inspect, and test periodically depending on climatic conditions.
- After confirming serviceability: switch off and repack.

---

## 6.5 Test Procedure — DMR HHPC

**Interval:** Once every six months.

### Standard Test Conditions

| Parameter | Value |
|---|---|
| Operational temperature | −20°C to +60°C |
| Storage temperature | −30°C to +70°C |
| Supply voltage | 7.5 V ± 0.1 V DC |
| Audio input frequency | 1000 Hz |
| Audio deviation | 5 kHz |
| RF input level | 5 µV (−93 dBm) |
| Volume control | Normal |
| Audio output termination | 8 Ω |
| RF termination | 50 Ω |
| Power mode | High power |

### Preliminary Visual / Manual Checks

- Equipment physically intact.
- All screws properly tightened.
- All accessories serviceable and in good condition.
- All controls operate smoothly; switch action is positive.
- All sockets serviceable and properly fitted.
- All parts free from dust, rust, moisture, oil, and grease.

---

# Part 7 — Operating Procedures

## 7.1 Turning the Radio On / Off

- Rotate the ON/OFF Volume Control knob **clockwise** until a click is heard to turn ON.
- Rotate **counter-clockwise** until a click is heard to turn OFF.

## 7.2 Adjusting Volume

- After power on: rotate the ON/OFF Volume Control knob clockwise to increase, counter-clockwise to decrease.

## 7.3 Selecting a Channel

- Rotate the Channel Selector knob to the desired channel.
- Display shows channel number and mode; frequency shown in admin mode.
- Channel frequencies configured via CPS.

## 7.4 Locking / Unlocking the Keypad

| Action | Key | Duration |
|---|---|---|
| Lock keypad (also turns off display) | `*` | Minimum 5 seconds |
| Unlock keypad | `#` | Minimum 5 seconds |

## 7.5 Placing a Call

- Press the PTT switch to transmit. Any radio tuned to the same frequency and mode will receive the transmission.

> **Note:** For optimal audio at the receiving radio, hold the radio approximately 2.5 to 5 cm from your mouth.

---

# Part 8 — Call Features

## Call Types in DMR Mode

- **Private Call:** Select call type `Private`; enter the Radio ID; hold PTT to transmit.
- **Group Call:** Select call type `GROUP`; enter the Group ID; hold PTT to transmit.
- **Broadcast Call:** Select call type `BROADCAST`; hold PTT to transmit to all radios on the same frequency.

## Modes of Operation

1. FM Half Duplex — Clear Voice
2. DMR Clear Voice and Data
3. DMR Secure Voice and Data

---

# Part 9 — Menu Structure and Features

## Main Menu Options

- DMR Features
- Messages
- Freq
- Accessories
- Settings

**Navigation:** Use `UP/DOWN` keys to select; press `SELECT` to open; press `BACK` to return.

---

## 9.1 DMR Features Menu

Options: BER Test, Radio Check, Radio Scan, Man-down, Radio Admin.

### 9.1.1 BER Test

Checks DMR sensitivity using a Radio Test Set instrument.

**Procedure:**
1. Select `BER Test`.
2. Select `ON` or `OFF` per ATP requirements.
3. Perform BER testing.
4. After testing, set option to `OFF`.

### 9.1.2 Radio Check

Checks availability of a desired radio within range.

**Procedure:**
1. Select `Radio Check`.
2. Enter the Radio ID.
3. Press `SET`.
- Result: user radio receives acknowledgement if the target radio is present.

### 9.1.3 Radio Scan

| Scan Type | Behavior |
|---|---|
| Priority Scan | Scans a channel assigned for priority |
| Normal Scan | Scans all channel frequencies |

### 9.1.4 Man Down

Standalone check of the man-down feature. Radio displays `Horizontal` or `Vertical` based on its physical position.

### 9.1.5 Radio Admin (Admin Mode)

**Access:** Enter password (configurable via CPS).

**Admin Mode Capabilities:**
- Manually set current channel frequency.
- Access to special radio features not available in normal mode.
- Feature configuration also possible through CPS.

**Admin Mode Display:** Shown on main screen while active.

**Lockout on failed attempts:** If admin password entered incorrectly 5 times, admin mode locks. Unlock requires re-entering the password through CPS.

**Admin Menu Options:** BB Integrity, RADIO, CRYPTO, Exit Admin.

#### BB Integrity

Displays the checksum of the baseband software for integrity verification.

#### RADIO Submenu

Options: Locate Radio, Radio Kill, Radio Enable, Radio Disable, Radio Monitor.

| Feature | Purpose | Procedure | Result |
|---|---|---|---|
| Locate Radio | Get GPS coordinates of another radio | Enter Radio ID | GPS coordinates sent; if unavailable: `GPS coordinates not found` |
| Radio Kill | Remotely erase target radio software | Select Radio Kill → Enter Radio ID → Select OK | Complete software erased; killed radio must return to factory for reprogramming |
| Radio Enable | Remotely enable a disabled radio | Enter Radio ID → Select OK | Radio enabled; restart recommended |
| Radio Disable | Remotely disable a radio | Enter Radio ID → Select OK | Target radio sends acknowledgement |
| Radio Monitor | Remotely monitor a radio | Enter Radio ID → Press OK | Monitoring duration configurable via CPS |

#### CRYPTO Submenu

**Access:** Password required.

Options: Chng Admin PWD, Reset Tamper, Test Mode, Algo Manage, Key Manage.

| Feature | Purpose |
|---|---|
| Chng Admin PWD | Change the admin password |
| Reset Tamper | Reset tamper status; tamper indicated by persistent `tampered` message on display after set is opened |
| Test Mode | Enable interoperability with existing sets in analog wideband mode; select `Analog WB`; return to original mode by changing and returning to channel |
| Algo Manage | Manage secure algorithm (load, erase, checksum, change password); password protected |
| Key Manage | Manage key-related operations (load, erase, checksums, buffer-to-active transfer, change password); password protected |

**Algo Manage Sub-options:**

| Option | Purpose |
|---|---|
| Algo Load | Load the algorithm into the radio |
| Algo Erase | Erase the algorithm from the radio |
| Algo Checksum | Verify algorithm data integrity via checksum |
| Chng Algo PWD | Change the Algo Manage password |

**Key Manage Sub-options:**

| Option | Purpose |
|---|---|
| Key Loading | Load key data from Child Fill Gun |
| Key Erase | Erase key data |
| Checksums | Check buffer key and active key checksums |
| Buff→Active | Transfer keys from buffer area to active keys (must be done after key loading for keys to be used) |
| Chng Key PWD | Change the Key Manage password |

---

## 9.2 Message Feature

Options: Compose, Inbox, Outbox, Quick Text.

### 9.2.1 Compose

Send messages to: Private Radio, Group ID, or Broadcast.

**Procedure:**
1. Compose the message.
2. Select Private Radio or Group ID.
3. Enter Radio ID or Group ID.
4. Send.

- To delete a wrongly typed character: press `UP` key.
- `UP` key deletion also applies during password entry.

### 9.2.2 Inbox

Displays received messages; select a message to read.

### 9.2.3 Outbox

Displays sent messages; select a message to review.

### 9.2.4 Quick Text Messages

1. Busy
2. Emergency
3. Can't call, txt
4. Call me later

---

## 9.3 Frequency

**Availability:** Admin mode only. User must enter admin mode first.

**Procedure (example — setting 147 MHz):**
```
Menu > DMR Features > Admin Mode
Back to Menu > Frequency > Enter Freq (147000000) > Select SET
```

Display shows: `Enter Freq`, `BACK`, `SET`.

---

## 9.4 Accessories Menu

Options: GPS, VOX.

### GPS

Displays GPS coordinates (Latitude, Longitude). Radio antenna must face open sky for GPS lock.

**Displayed parameters:** GPS CO-ORD, Time, Latitude, Longitude, Fix status, Satellite count.

### VOX

Enables hands-free operation. Voice is detected automatically; PTT button not required.

---

## 9.5 Settings Menu

Options: LONE WORKER / MANDOWN, DCDM, SQUELCH, PA.

### Lone Worker / Mandown

Timeout duration configured via CPS software.

### DCDM (Dual Capacity Direct Mode)

**Enable:** Menu → Settings → DCDM → select `SLOT 1` or `SLOT 2`.
- Radio reconfigures automatically; display shows `SLOT-1 Enabled` (or equivalent).

**Disable:** Menu → Settings → DCDM → select `DCDM OFF`.

### Squelch

Operates in analog mode only.

| Option | Behavior |
|---|---|
| SQL ON | Squelch active; level adjustable |
| SQL OFF | Squelch disabled |

### PA (Power Output Level)

| Option | Output Power | Menu Path |
|---|---|---|
| HIGH | 5 W | Menu → Settings → PA → HIGH |
| LOW | 1 W | Menu → Settings → PA → LOW |

Default power option for all channels configurable via CPS.

---

# Part 10 — Keypad Controls

| Key | Numeric Input | Alphabetic / Special Input |
|---|---|---|
| KEY 1 | `1` | `@`, `/` |
| KEY 2 | `2` | `a`, `b`, `c` |
| KEY 3 | `3` | `d`, `e`, `f` |
| KEY 4 | `4` | `g`, `h`, `i` |
| KEY 5 | `5` | `j`, `k`, `l` |
| KEY 6 | `6` | `m`, `n`, `o` |
| KEY 7 | `7` | `p`, `q`, `r`, `s` |
| KEY 8 | `8` | `t`, `u`, `v` |
| KEY 9 | `9` | `w`, `x`, `y`, `z` |
| KEY 10 | `0` | — |

Applicable contexts: entering frequency, entering password, typing messages.

---

# Part 11 — DMR CPS (Customer Programming Software)

## Overview

CPS (Customer Programming Software) configures and programs DMR devices. Used to set radio parameters, channels, contacts, and features per operational requirements.

## CPS Tabs

- General
- VHF Channel Configuration
- Misc Features
- Contact Lists

## Login

Open CPS → login screen displayed → enter provided Username and Password.

---

## General Tab

Contains: Serial Port Section, Radio Information Section, Side Key Programming Section, Tx Timeout Programming, Display Radio Parameters, Bottom Left Buttons.

### Serial Port Section

- COM Port selection and Baud Rate configuration.
- Baud Rate: `38400`.
- Select the COM port where the radio programming cable is connected.

### Radio Information Section

- Radio Name, Radio ID.
- Admin Password, Power ON Password.

### Side Key Programming Section

| Key | Assignable Options |
|---|---|
| Side Key 1 | Power, Squelch, Backlight |
| Side Key 2 | Power, Squelch, Backlight |

- If `Power` is assigned: key press toggles RF output between Low Power and High Power.

### Tx Timeout Programming

TOT (Time-Out Timer) prevents a user from occupying a channel beyond the preset time. Radio automatically terminates transmission when TOT expires.

### Display Radio Parameters

- Select Radio ID; open file data using the `File Data` button.

### Bottom Left Buttons

| Button | Function |
|---|---|
| Save All | Saves all settings |
| Send All | Sends all configuration to the radio |
| Read All | Reads existing settings from the radio |
| Send Checksum | Verifies data integrity before sending |

---

## VHF Channel Configuration Tab

| Parameter | Options / Values |
|---|---|
| Channel Type | Digital (all channels) |
| Channel Name | ch-0 through ch-1520 |
| Tx Frequency | Configurable |
| Rx Frequency | Configurable |
| Tx Power | LOW or HIGH |
| Rx Only | Disabled (default); enable to restrict to receive-only |
| Color Code | `0` or `1` (channel separation) |
| Slot Option | Slot 1 (example); TDMA-based; used to assign different time slots per channel |
| Encryption Type | CLEAR (unsecured communication) or CUSTOM (secured communication) |

---

## Misc Features Tab

Contains: DMR Feature, Timeout Programming Section, VoX Parameters, Messages.

### DMR Feature

Enabled/disabled via checkboxes:
- Remote Radio Check
- Remote Radio Monitor
- Remote Radio Disable
- Remote Kill
- GPS Tracking

### Timeout Programming Section

Configures timers for: Radio Monitor, Lone Worker, Mandown.

### VoX Parameters

| Parameter | Function |
|---|---|
| VoX Sensitivity | Controls how easily the radio activates on voice input |
| VoX Timeout | Delay (seconds) before VOX stops transmitting after voice input ends |

### Messages

Contains pre-programmed quick text messages for use from the radio.

---

## Contact Lists Tab

### Group List

Manages group contacts the radio is a member of. Radio listens to all communications for listed groups.

### Contact List

Stores individual radio contacts.

---

# Part 12 — Dismantling, Reassembly, and Component Replacement

## General Precautions

- Polarized connectors prevent incorrect interchange.
- Tag and mark disconnected wires with identification marks before disconnecting.
- Seat modules on rivet spacers/guides and confirm connector mating before tightening.
- Refer drawing **GA 1710 005 801 63 (Sheets 1 to 5)** for dismantling and reassembly procedures.

## Electronic Component Handling

- Exercise special care with ICs, discrete components, and other electronic components.
- Use only a **miniature soldering iron**.
- Maintain high soldering quality standards.
- Disturb circuit wiring as little as possible.

## Component Removal and Replacement Procedure

1. Use a **low-wattage soldering iron**.
2. Use **antistatic tools** throughout.
3. Before removing ICs, use a **de-solder gun** to remove solder from IC pins.
4. Pull out ICs using **pullers** only (do not use force).
5. When installing ICs: use **IC inserts**, then solder.
6. **Do not touch CMOS, MOS, or ICs with bare hands** (static-sensitive components).


# Chapter 3 — Fault Diagnosis and Troubleshooting

## Overview

The Radio Set has a modular physical design. Faults are isolated by identifying the faulty module. Effective repair requires knowledge of the system's operational architecture.

> **⚠️ CRITICAL SAFETY CAUTION**
> **ENSURE THE RADIO SET IS COMPLETELY SWITCHED OFF WHILE REPLACING MODULES OR CONNECTORS DURING TROUBLESHOOTING.**

For deeper hardware servicing, refer to *Technical Mechanical Part III: Overhaul and Reconditioning Instructions*.

---

## Troubleshooting Procedure Index

| Procedure | Condition to Apply |
|---|---|
| Procedure 1 | Radio set is completely dead (will not turn ON) |
| Procedure 2 | Module failure check via internal diagnostics (iBITE) |
| Procedure 3 | Display errors or keypad input faults |
| Procedure 4 | No reception / bad received audio |
| Procedure 5 | Transmission not working |

---

## Procedure 1 — Dead Unit Troubleshooting

**Symptom:** Handheld terminal fails to turn ON.

### Step 1 — Battery Voltage Check

- **Action:** Check battery voltage to confirm the battery is charged.
- **If voltage is low:** Charge the battery.
- **If voltage is sufficient:** Proceed to Step 2.

### Step 2 — Main Power Interface Test (TP 34)

- **Action:** Measure voltage at test point **TP 34**.
- **Expected value:** `~7.4 V` (nominal battery voltage).
- **If voltage is absent or incorrect:** Battery connection is faulty.
- **If voltage is correct:** Proceed to Step 3.

### Step 3 — Core Regulator Rails Test (TP 35 / TP 36)

- **Action:** Measure voltage at **TP 35** and **TP 36**.
- **Expected values:** **TP 35** = `3.6 V`; **TP 36** = `5 V`.
- **If rails are absent or incorrect:** **U24** power component is faulty.
- **If rails are correct:** Proceed to Step 4.

### Step 4 — Logic Supply Check (R55)

- **Action:** Measure voltage at resistor **R55**.
- **Expected value:** `3.3 V`.
- **If 3.3 V line is absent:** Evaluate downstream components.
- **If 3.3 V line is present:** **U29** component is faulty.

### Step 5 — Display Execution Verification

- **Condition:** Core power steps are valid but screen remains unresponsive.
- **Root cause:** Display assembly is faulty.
- **Action:** Validate the display assembly using a specialized test jig.

---

## Procedure 2 — BITE Check Matrix (iBITE Diagnostics)

**Purpose:** Check for module failure using internal diagnostics.

### Step 1 — Initial Setup

1. Connect the battery to the Radio Set.
2. Connect the antenna to the Radio.
3. Switch on the Radio Set.
4. Navigate to the menu and select **iBITE**.

### Step 2 — Baseband Layer Test

- **Display condition:** Does the display show **`BB:OK`**?
- **If No:** In the Baseband card, reprogram the SCT.
- **If Yes:** Proceed to Step 3.

### Step 3 — RF Layer Test

- **Display condition:** Does the display show **`RF:OK`**?
- **If No:**
  - Check the RF path and reprogram the SCT.
  - Possible causes: RTC (Real-Time Clock) may be faulty, or SPI flash may be faulty in the SM Card.
- **If Yes:** Proceed to Step 4.

### Step 4 — FPGA Status Check

- **Display condition:** Does the display show **`F:1`**?
- **If Yes:** FPGA may be faulty in the SM card.
- **If No:** Proceed to Step 5.

### Step 5 — SPI Flash Status Check

- **Display condition:** Does the display show **`S:1`**?
- **If Yes:** SPI flash may be faulty in SM card.
- **If No:** Proceed to Step 6.

### Step 6 — RTC Status Check

- **Display condition:** Does the display show **`R:1`**?
- **If Yes:** RTC may be faulty in SM card.
- **If No:** Built-in diagnostics check has passed. No active module faults detected.

---

## Procedure 3 — Display / Keypad Subsystem Troubleshooting

**Symptom:** Problem with display rendering or keypad input.

### Step 1 — Initial Power Setup

1. Connect the battery to the Radio Set.
2. Connect the antenna to the Radio.
3. Switch on the Radio.

### Step 2 — Visual Character Verification

- **Condition:** Does the display show proper characters?
- **If Yes:** Proceed to Step 4 (Keypad Input Diagnostics).
- **If No:** Proceed to Step 3.

### Step 3 — Display Rendering Diagnostics

- **Condition:** Is the display missing or showing unwanted characters?
- **If Yes:** Check proper connection of the display cable, or the display itself is faulty.
- **If No:** Display is confirmed functional.

### Step 4 — Keypad Input Diagnostics

- **Action:** Navigate to **Menu → Message → Compose** and check all keys.
- **Condition:** Is digit display proper?
- **If No:** Keypad or keypad cable is faulty.
- **If Yes:** Keypad and display are confirmed fully functional.

---

## Procedure 4 — Receiver Path (Rx) Troubleshooting

**Symptom:** No reception / bad SINAD / no recovered audio.

### Step 1 — RSSI Display Test

- **Action:** Apply RF signal and observe the RSSI indicator on display.
- **Condition:** Is the RSSI sign displayed when RF is turned on?
- **If Yes:** Proceed to Audio Subsystem Path (Step 2).
- **If No:** Proceed to Local Oscillator Path (Step 3).

### Step 2 — Audio Subsystem Path

- **Action:** Check audio signal at **C21**.
- **Condition:** Is audio present at C21?
- **If Yes:** Check the speaker.
- **If No:** Further audio path diagnosis required.

### Step 3 — Local Oscillator (L.O.) Verification

- **Action:** Check L.O. frequency at **C114**.
- **Expected value:** Double the channel frequency.
- **If correct frequency:** Proceed to Regulator Rails Test (Step 5).
- **If incorrect frequency:** Proceed to Master Clock Check (Step 4).

### Step 4 — Master Clock Check (U38)

- **Action:** Check for `38.4 MHz` signal at **U38**.
- **If correct frequency:** No downstream path specified; evaluate local trace.
- **If incorrect frequency:** **TCXO** is faulty.

### Step 5 — Regulator Rails Test (L37)

- **Action:** Measure voltage at **L37**.
- **Expected value:** `1.2 V`.
- **If voltage is correct:** **U4** is faulty.
- **If voltage is incorrect:** **U21** is faulty.

---

## Procedure 5 — Transmitter Path (Tx) Troubleshooting

**Symptom:** TX not working.

### Step 1 — PTT / LED Observation

- **Action:** Press the PTT switch and observe the status LED.
- **If RED LED does not glow:** Proceed to Branch A — LED Fault Logic.
- **If RED LED glows:** Proceed to Branch B — RF Power Logic.

---

### Branch A — LED Fault Logic (RED LED Does Not Glow)

**Step 2 — PTT Switch Mechanical Check (SW 5)**

- **Action:** Check whether **SW 5** shorts when pressed.
- **If No:** **SW 5** is faulty.
- **If Yes:** Proceed to Step 3.

**Step 3 — Controller Line Toggling Check (R248)**

- **Action:** Check for toggling at **R248** when PTT is pressed.
- **If No:** Controller is faulty.
- **If Yes:** Proceed to Step 4.

**Step 4 — Regulator Rail Check (L37)**

- **Action:** Measure voltage at **L37**.
- **Expected value:** `1.2 V`.
- **If voltage is absent:** **U21** is faulty.
- **If voltage is present:** **U4** is faulty.

---

### Branch B — RF Power Logic (RED LED Glows)

**Step 5 — Reference Clock Distribution Check (L42)**

- **Action:** Check for `38.4 MHz` signal at inductor **L42**.
- **If No signal:** **U38** is faulty.
- **If signal present:** Proceed to Step 6.

**Step 6 — Transmitter Line Toggling Check (R179)**

- **Action:** Check for toggling at **R179** when PTT is pressed.
- **If No toggling:** **U4** is faulty.
- **If toggling present:** All specified component diagnostic checks passed; evaluate secondary downstream matching network blocks.

---

## Fault Summary Reference

| Symptom / Check Point | Expected Value | Faulty Component |
|---|---|---|
| TP 34 — no voltage | `~7.4 V` | Battery connection |
| TP 35 — no/wrong voltage | `3.6 V` | U24 |
| TP 36 — no/wrong voltage | `5 V` | U24 |
| R55 — 3.3 V absent, U29 path | `3.3 V` | U29 |
| Screen unresponsive after power valid | — | Display assembly |
| iBITE: BB not OK | `BB:OK` | Baseband SCT — reprogram |
| iBITE: RF not OK | `RF:OK` | RF path SCT / RTC / SPI flash in SM Card |
| iBITE: F:1 displayed | `F:0` | FPGA in SM card |
| iBITE: S:1 displayed | `S:0` | SPI flash in SM card |
| iBITE: R:1 displayed | `R:0` | RTC in SM card |
| RSSI absent; C114 — wrong L.O. freq; U38 — wrong | `38.4 MHz` | TCXO |
| RSSI absent; C114 correct; L37 correct | `1.2 V` | U4 |
| RSSI absent; C114 correct; L37 incorrect | `1.2 V` | U21 |
| TX: RED LED absent; SW5 no short | — | SW 5 |
| TX: RED LED absent; R248 no toggle | — | Controller |
| TX: RED LED absent; L37 absent | `1.2 V` | U21 |
| TX: RED LED absent; L37 present | `1.2 V` | U4 |
| TX: RED LED present; L42 no 38.4 MHz | `38.4 MHz` | U38 |
| TX: RED LED present; R179 no toggle | — | U4 |
