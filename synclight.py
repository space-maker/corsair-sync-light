from PIL import ImageGrab
import time

class Screenshot:
    def __init__(self):
        self.img = None

        self.size_x = None
        self.size_y = None

    def take_screen(self):
        self.img = ImageGrab.grab()
        self.size_x, self.size_y = self.img.size

    def mean_frequencies_color(self, max_row, max_column, current_row, current_column):
        r, g, b = 0, 0, 0
        count_colors = (int((current_row + 1) * self.size_x / max_row) * self.size_x - int(current_row * self.size_x / max_row) + 1) *\
                       (int((current_column + 1) * self.size_y / max_column) - int(current_column * self.size_y / max_column) + 1)
        n=0
        for x in range(int(current_row * self.size_x / max_row), int((current_row + 1) * self.size_x / max_row), 1000):
            for y in range(int(current_column * self.size_y / max_column), int((current_column + 1) * self.size_y / max_column), 1000):
                rgb = self.img.getpixel((x, y))
                r += rgb[0]
                g += rgb[1]
                b += rgb[2]
                n += 1

        # print(count_colors, n)
        r //= n
        g //= n
        b //= n

        return (r, g, b)

class SyncLightCorsair:
    def __init__(self, keyboard):
        self._keyboard = keyboard

    def ambilight(self):
        sc = Screenshot()
        sc.take_screen()

        max_row = self._keyboard.slices_keyboard
        current_row = 0

        for row, max_column in self._keyboard:
            for current_column in range(max_column):
                rgb_color = sc.mean_frequencies_color(max_row, max_column, current_row, current_column)
                row(current_column, rgb_color)

            current_row += 1

        self._keyboard.apply_colors()
        

    def runtest(self):
        for row, columns in self._keyboard:
            for column in range(columns):
                row(column, (255, 255, 255))
                time.sleep(0.01)
                self._keyboard.apply_colors()
