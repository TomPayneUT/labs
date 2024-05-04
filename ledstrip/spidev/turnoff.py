from lib import neopixel_spidev as np

with np.NeoPixelSpiDev(0, 0, n=56, pixel_order=np.GRB) as pixels:
        pixels.fill(0)
        pixels.show()