```text
  ▄▄▄                          ▄▄                 
 █▀██  ██  ██▀▀                 ██                
   ██  ██  ██                   ██ ▀▀       ▄▄    
   ██  ██  ██ ▄▀▀█▄ ██ ██ ▄███▀ ██ ██ ▄███▀ ██ ▄█▀
   ██▄ ██▄ ██ ▄█▀██ ██▄██ ██    ██ ██ ██    ████  
   ▀████▀███▀▄▀█▄██▄▄▀██▀▄▀███▄▄██▄██▄▀███▄▄██ ▀█▄
                      ██                          
                    ▀▀▀                           
```

# WAYCLICK

Minimal, low-latency auto-clicker built for Linux, Wayland and power users.

WAYCLICK uses `evdev` + `uinput` to create native virtual mouse events directly through the Linux input subsystem — no X11 hacks, no GUI dependency, no Electron bloat.

Designed for:

* Wayland
* KDE Plasma
* Hyprland
* tiling WMs
* low RAM usage
* ultra-fast click intervals

---

# Features

* Native Linux input injection (`uinput`)
* Works on Wayland
* Extremely lightweight
* Toggle mode
* Left/right click support
* Precise timing loop
* Single-file architecture
* Zero GUI frameworks
* No root required after proper udev setup
* Minimal terminal interface

---

# Why WAYCLICK?

Most Linux auto-clickers:

* depend on X11
* break on Wayland
* use bloated GUI frameworks
* rely on unreliable automation APIs

WAYCLICK talks directly to the Linux input layer.

Result:

* lower latency
* lower overhead
* Wayland compatibility
* more reliable behavior

---

# Requirements

## System

* Linux
* Python 3.10+
* `/dev/uinput` access

## Python dependencies

```bash
pip install evdev
```

---

# UInput Setup (Required)

To run WAYCLICK without `sudo`, configure `uinput` permissions.

## 1. Create udev rule

```bash
echo 'KERNEL=="uinput", GROUP="uinput", MODE="0660", OPTIONS+="static_node=uinput"' | sudo tee /etc/udev/rules.d/99-uinput.rules
```

## 2. Create group and add your user

```bash
sudo groupadd uinput
sudo usermod -aG uinput $USER
```

## 3. Reload udev rules

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

Then:

* logout/login
  or
* reboot

---

# Usage

Run:

```bash
python wayclick.py
```

The application will ask for:

* CPS
* mouse button

Example:

```text
CPS (default 20): 100
button (left/right): left
```

After startup:

* Press ENTER to toggle clicking
* Press CTRL+C to exit

---

# Performance

Typical RAM usage:

* ~8MB to ~25MB
  (depending on Python runtime and distro)

CPU usage:

* extremely low at normal CPS
* scales with click interval precision

WAYCLICK uses:

* threaded timing loop
* monotonic high-resolution timers
* direct event injection

No polling-heavy GUI frameworks are used.

---

# Technical Details

WAYCLICK creates a virtual mouse device using Linux `uinput`.

Clicks are emitted through:

* `EV_KEY`
* `BTN_LEFT`
* `BTN_RIGHT`

Timing uses:

* `time.perf_counter()`
* drift correction loop

This avoids the timing instability common in naive `sleep()` implementations.

---

# Compatibility

## Tested

* KDE Plasma Wayland
* Arch Linux

## Expected to work

* Hyprland
* Sway
* GNOME Wayland
* X11 environments

---

# Philosophy

WAYCLICK is intentionally:

* minimal
* transparent
* hackable
* dependency-light

No telemetry.
No background services.
No unnecessary UI.

Just clicks.

---

# Roadmap

Planned:

* configurable hotkeys
* JSON config
* packaged releases
* AUR package
* daemon mode
* multiple click profiles
* live CPS switching
* Rust rewrite experiment

---

# Disclaimer

Use responsibly.

Some games and anti-cheat systems may detect synthetic input devices generated through `uinput`.

WAYCLICK is intended for automation, accessibility, testing and personal workflow usage.
