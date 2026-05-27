import time
import threading
import argparse
from evdev import UInput, ecodes as e


class AutoClicker:
    def __init__(self, interval, button, mode, hold_keycode=None):
        self.interval = interval / 1000.0
        self.button = e.BTN_LEFT if button == "left" else e.BTN_RIGHT
        self.mode = mode  # hold | toggle

        self.active = False
        self.holding = False

        self.hold_keycode = hold_keycode

        capabilities = {
            e.EV_KEY: [e.BTN_LEFT, e.BTN_RIGHT],
        }

        self.device = UInput(capabilities, name="auto-clicker")

        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()

    # ---------------- CLICK ----------------
    def click(self):
        self.device.write(e.EV_KEY, self.button, 1)
        self.device.syn()
        self.device.write(e.EV_KEY, self.button, 0)
        self.device.syn()

    # ---------------- LOOP ----------------
    def loop(self):
        next_time = time.perf_counter()

        while True:
            if self.is_active():
                self.click()

            next_time += self.interval
            sleep_time = next_time - time.perf_counter()

            if sleep_time > 0:
                time.sleep(sleep_time)

    # ---------------- STATE ----------------
    def is_active(self):
        if self.mode == "toggle":
            return self.active
        return self.holding

    # ---------------- INPUT CONTROL (manual API) ----------------
    def set_hold(self, state: bool):
        self.holding = state

    def toggle(self):
        self.active = not self.active
        print(f"[AUTOCLICKER] {'ON' if self.active else 'OFF'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--ms", type=float, default=50)
    parser.add_argument("--button", choices=["left", "right"], default="left")
    parser.add_argument("--mode", choices=["hold", "toggle"], default="hold")

    args = parser.parse_args()

    clicker = AutoClicker(
        interval=args.ms,
        button=args.button,
        mode=args.mode
    )

    print("AutoClicker rodando")
    print("Modo:", args.mode)
    print("Intervalo:", args.ms, "ms")

    if args.mode == "hold":
        print("Pressione ENTER para ativar/desativar HOLD")

        while True:
            input()
            clicker.set_hold(not clicker.holding)
            print("HOLD:", clicker.holding)

    else:
        print("Pressione ENTER para toggle ON/OFF")

        while True:
            input()
            clicker.toggle()