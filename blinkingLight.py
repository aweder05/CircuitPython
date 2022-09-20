import board
import neopixel
import time 
import math 

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1 #sets the brightness level of the LED

print("Make it red!") #prints "" onto the serial monitor

while True: #coontinuously blinks a red led, with 2/10 second intervals
    dot.fill((255, 0, 0))
    time.sleep (0.2)
    dot.fill((0, 0, 255))
    time.sleep (0.2)