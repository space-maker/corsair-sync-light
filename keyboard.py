class Keyboard:
    def __init__(self, sdk, keysmap):  
        self._sdk = sdk  
        self._sdk.request_control()

        self._keysmap = keysmap
        self.current_iterator = 0

        self.slices_keyboard = len(keysmap)
    
    def set_color(self, coordinate, rgb_color):
        x, y = coordinate
        self._sdk.set_led_colors_buffer_by_device_index(0, {self._keysmap[x][y]: rgb_color})

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_iterator >= self.slices_keyboard:
            self.current_iterator = 0
            raise StopIteration

        ret = self.current_iterator
        self.current_iterator += 1

        return (lambda coordinate_y, rgb_color: self.set_color((ret, coordinate_y), rgb_color), len(self._keysmap[ret]))

    def set_color_row(self, row, coordinate, rgb_color):
        pass

    def apply_colors(self):
        self._sdk.set_led_colors_flush_buffer()
