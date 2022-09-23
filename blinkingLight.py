As my first Circuit Python Assignment, the hardest part was setting up Visual Studio code to be compatible with the board that we’re using. 
Other than that, the code was very simple and I pretty much got most of it from the internet. 
What I would do differently next time would be to follow directions more closely and more logically. 
It would save a lot of time and would help me budget more time into trying to do other things with the assignments. 


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
