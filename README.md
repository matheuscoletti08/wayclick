# Wayclick

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

Minimal low-latency auto-clicker for Linux and Wayland.

Direct Linux input injection using evdev/uinput.

Built with:

* Python
* evdev
* uinput

Designed for:

* KDE Plasma
* Hyprland
* Wayland
* tiling window managers
* low overhead
* fast click timing

---

## Features

* Native Linux input injection
* Wayland compatible
* Low latency
* Lightweight
* Left/right click support
* Toggle mode
* Minimal terminal UI
* No GUI frameworks
* No X11 requirement

---

## Installation

Clone the repository:

```bash
git clone https://github.com/matheuscoletti08/Wayclick.git
cd Wayclick
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate venv:

### Bash/Zsh

```bash
source .venv/bin/activate
```

### Fish

```fish
source .venv/bin/activate.fish
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## UInput Setup

Wayclick requires access to `/dev/uinput`.

Create udev rule:

```bash
echo 'KERNEL=="uinput", GROUP="uinput", MODE="0660", OPTIONS+="static_node=uinput"' | sudo tee /etc/udev/rules.d/99-uinput.rules
```

Create group and add your user:

```bash
sudo groupadd uinput
sudo usermod -aG uinput $USER
```

Reload rules:

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

Then reboot or relog.

---

## Usage

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

Controls:

```text
ENTER   -> toggle clicking
CTRL+C  -> exit
```

---

## Requirements

System:

* Linux
* Python 3.10+
* uinput access

Python:

* evdev

---

## Performance

Typical memory usage:

* ~8MB to ~25MB RAM

Designed to remain lightweight even at high CPS values.

---

## Compatibility

Tested on:

* CachyOS
* KDE Plasma Wayland

Expected to work on:

* Hyprland
* GNOME Wayland
* Sway
* X11

---

## Roadmap

Planned:

* configurable hotkeys
* config.json support
* packaged releases
* AUR package
* live CPS switching
* daemon mode

---

## License

MIT License
