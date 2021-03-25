from cuesdk import CorsairLedId, CueSdk

import keyboard
import synclight
import json
from time import perf_counter, sleep
from os import system
import sys
import threading
import signal


class SyncLightCorsairHandler:
    def __init__(self):
        self._sdk = CueSdk()
        self._config_keys = None
        self._fps = 0
        
    def init(self):
        if not self._sdk.connect():
            raise Exception("sdk is disabled")

        with open("config_keys.json") as filename_config_file:
            self._config_keys = json.loads(filename_config_file.read())

    def run(self, ambilight_mode, keyboard_model, keyboard_mode):
        keysmap = list(map(self._map_keys, self._config_keys[keyboard_model]["keys"][keyboard_mode]))
        sync = synclight.SyncLightCorsair(keyboard.Keyboard(self._sdk, keysmap))
        verbose_threading = threading.Thread(target=self._verbose_threading)
        verbose_threading.start()

        try:
            while True:
                begin = perf_counter()
                sync.ambilight()
                self._fps = 1.0 / (perf_counter() - begin)
        except (KeyboardInterrupt, SystemExit):
            self._fps = -1
            sleep(1)
            sys.quit(1)

    def _verbose_threading(self):
        clear = lambda: system('cls')
        while self._fps >= 0:
            print(self._fps, "fps")
            sleep(1)
            clear()
        
    def _map_keys(self, row):
        return list(map(lambda key: getattr(CorsairLedId, "K_" + key), row))

if __name__ == "__main__":
    sync = SyncLightCorsairHandler()
    sync.init()

    sync.run("individual", "K95", "azerty")
