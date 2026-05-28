import time
import threading
from evdev import UInput, ecodes


ASCII = r"""
  ▄▄▄                          ▄▄                 
 █▀██  ██  ██▀▀                 ██                
   ██  ██  ██                   ██ ▀▀       ▄▄    
   ██  ██  ██ ▄▀▀█▄ ██ ██ ▄███▀ ██ ██ ▄███▀ ██ ▄█▀
   ██▄ ██▄ ██ ▄█▀██ ██▄██ ██    ██ ██ ██    ████  
   ▀████▀███▀▄▀█▄██▄▄▀██▀▄▀███▄▄██▄██▄▀███▄▄██ ▀█▄
                      ██                          
                    ▀▀▀                           
"""


class Clicker:
    def __init__(self, cps: int, button: str):
        self.cps = max(1, cps)
        self.delay = 1 / self.cps

        self.active = False

        self.button = (
            ecodes.BTN_LEFT
            if button == "left"
            else ecodes.BTN_RIGHT
        )

        self.device = UInput(
            {
                ecodes.EV_KEY: [
                    ecodes.BTN_LEFT,
                    ecodes.BTN_RIGHT
                ]
            },
            name="wayclicker"
        )

        threading.Thread(
            target=self.loop,
            daemon=True
        ).start()

    def click(self):
        self.device.write(
            ecodes.EV_KEY,
            self.button,
            1
        )
        self.device.syn()

        self.device.write(
            ecodes.EV_KEY,
            self.button,
            0
        )
        self.device.syn()

    def loop(self):
        next_t = time.perf_counter()

        while True:
            if self.active:
                self.click()

                next_t += self.delay

                sleep = next_t - time.perf_counter()

                if sleep > 0:
                    time.sleep(sleep)
                else:
                    next_t = time.perf_counter()

            else:
                time.sleep(0.01)


def render(clicker, button):
    print("\033[H\033[J", end="")

    status = (
        "ON"
        if clicker.active
        else "OFF"
    )

    print(ASCII)

    print(f"CPS: {clicker.cps}")
    print(f"BUTTON: {button}")
    print(f"STATUS: {status}")

    print("\nENTER = toggle")
    print("CTRL+C = exit")


def main():
    cps = input("CPS (default 20): ").strip()
    cps = int(cps) if cps else 20

    button = input(
        "button (left/right): "
    ).strip().lower()

    if button not in ["left", "right"]:
        button = "left"

    clicker = Clicker(cps, button)

    try:
        while True:
            render(clicker, button)

            input()

            clicker.active = not clicker.active

    except KeyboardInterrupt:
        print("\nEXIT")


if __name__ == "__main__":
    main()