import time
import board
import neopixel_spi as neopixel
from itertools import cycle
from sys import argv

NUM_PIXELS = int(15)
PIXEL_ORDER = neopixel.GRB
COLORS = (0xFF0000, 0x00FF00, 0x0000FF)
DELAY = 0.1
spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, bpp=3, brightness=0.1, pixel_order=PIXEL_ORDER, auto_write=True
)

def rainbow_effect():
    color_cycle = cycle(COLORS)

    for color in color_cycle:
        pixels.fill(color)
        time.sleep(DELAY)

if __name__ == "__main__":
    pixels.fill(0)
    try:
        rainbow_effect()
    except KeyboardInterrupt:
        raise
    finally:
        pixels.fill(0)