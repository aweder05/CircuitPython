# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time 
import board
import adafruit_hcsr04 #imports the file that allows the HC-SR04 to work

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        print((sonar.distance)) #reads the sonar distance from the 
                                #sensor and prints it into the serial monitor
    except RuntimeError: #if there is a runtime error:
        print("Retrying!") #:prints, "retrying" to the serial monitor
    time.sleep(0.1) #delays the loop for one tenth of a second to prevent 
                    #an overflow in the serial monitor 