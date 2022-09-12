import board
import neopixel
import time 
import math 

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1

print("Make it red!")

while True:
    dot.fill((255, 0, 0))
    time.sleep (0.2)
    dot.fill((0, 0, 255))
    time.sleep (0.2)