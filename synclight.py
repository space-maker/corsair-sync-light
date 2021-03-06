import time
import d3dshot

class Screenshot:
    def __init__(self):
        self.img = None

        self.size_x = None
        self.size_y = None
        self.d = d3dshot.create(capture_output="numpy")

    def take_screen(self):
        self.img = self.d.screenshot()
        self.size_x, self.size_y = len(self.img[0]), len(self.img)

    def mean_frequencies_color(self, max_row, max_column, current_row, current_column, wordload=100):
        r, g, b = 0, 0, 0
    
        sample_x = wordload
        sample_y = wordload
        
        n = 0
        for x in range(int(current_row * self.size_y / max_row), int((current_row + 1) * self.size_y / max_row), sample_y):
            for y in range(int(current_column * self.size_x / max_column), int((current_column + 1) * self.size_x / max_column), sample_x):
                rgb = self.img[x][y]
                r += rgb[0]
                g += rgb[1]
                b += rgb[2]
                
                n += 1

        r //= n
        g //= n
        b //= n

        return (r, g, b)

class SyncLightCorsair:
    def __init__(self, keyboard):
        self._keyboard = keyboard
        self.sc = Screenshot()

    def ambilight(self, mode="mean_frequencies_color"):
        self.sc.take_screen()

        max_row = self._keyboard.slices_keyboard
        current_row = 0

        for row, max_column in self._keyboard:
            for current_column in range(max_column):
                rgb_color = getattr(self.sc, mode)(max_row, max_column, current_row, current_column)
                row(current_column, rgb_color)

            current_row += 1

        self._keyboard.apply_colors()
        

    def runtest(self):
        for row, columns in self._keyboard:
            for column in range(columns):
                row(column, (255, 0, 255))
                time.sleep(0.01)
                self._keyboard.apply_colors()
