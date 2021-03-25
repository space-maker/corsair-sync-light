from cuesdk import CorsairLedId, CueSdk

import keyboard
import synclight
import json
from time import perf_counter
from os import system

class SyncLightCorsairHandler:
    def __init__(self):
        self._sdk = CueSdk()
        self._config_keys = None
        
    def init(self):
        if not self._sdk.connect():
            raise Exception("sdk is disabled")

        with open("config_keys.json") as filename_config_file:
            self._config_keys = json.loads(filename_config_file.read())

    def run(self, ambilight_mode, keyboard_model, keyboard_mode):
        keysmap = list(map(self._map_keys, self._config_keys[keyboard_model]["keys"][keyboard_mode]))
        sync = synclight.SyncLightCorsair(keyboard.Keyboard(self._sdk, keysmap))
        # sync.runtest()

        while True:
            begin = perf_counter()
            sync.ambilight()

            system("cls")
            print(1 / (perf_counter() - begin), "fps")

    def _map_keys(self, row):
        return list(map(lambda key: getattr(CorsairLedId, "K_" + key), row))

if __name__ == "__main__":
    sync = SyncLightCorsairHandler()
    sync.init()

    sync.run("individual", "K95", "azerty")
