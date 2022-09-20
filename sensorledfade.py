# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import digitalio
import simpleio
import time
import board
import adafruit_hcsr04
import neopixel                       
from board import *

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
Anton = neopixel.NeoPixel(board.NEOPIXEL, 1)#connecting the neopixel on the board to the code
Anton.brightness = 0.1
1  #setting the brightness of the light, from 0-1 brightness
AntonOutput = 0
Red = 0
Green = 0
Blue = 0

while True:
    try:
        cm = sonar.distance 
        print((sonar.distance, Red, Green, Blue))
        time.sleep(0.1)
        if cm < 5: #turns the LED a certain color if the distance is less than 5 cm 
            Blue = 0
            Red = 255
            Anton.fill((Red, 0, 0))#setting the color with RGB values
        if cm > 5 and cm < 10: #turns the LED a certain color if the distance is  
            Green = 0          #between 5 and 10 cm
            Red = simpleio.map_range(cm, 5.1, 10, 255, 0)
            Blue = simpleio.map_range(Red, 0, 255, 255, 0)
            Anton.fill((Red, Green, Blue))
        else: #if the distance is anything else, do the following:
            
            Blue = simpleio.map_range(cm, 10.1, 20, 255, 0)
            Green = simpleio.map_range(Blue, 0, 255, 255, 0)
            Anton.fill((0, Green, Blue))#setting the color with RGB values
    except RuntimeError: #if there is a runtime error
        print("Retrying!") #print "retrying" to the serial monitor
    time.sleep(0.01) #delays the whole loop for one tenth of a second