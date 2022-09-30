# CircuitPython

## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_DistanceSensor](#CircuitPython_DistanceSensor)
* [CircuitPython_LCD](#CircuitPython_LCD)
---

## Hello_CircuitPython

### Description & Code
The purpose of this assignment is to get the serial monitor to print "Hello World"

```python
from time import sleep

while True:
    print("Hello World!") ##Prints "Hello World!" to the serial monitor
    sleep(1)

```


### Evidence

![name](https://github.com/aweder05/CircuitPython/blob/master/media/helloworld.gif.gif?raw=true)

And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring

The wiring of this assignment is quite literally just plugging in the board into one of the USB ports on the Computer

![name](https://github.com/aweder05/CircuitPython/blob/master/media/helloworldwiring.jpg?raw=true)

Image credit goes to [Adafruit Industries](https://www.adafruit.com/product/4000)

### Reflection

The hardest part about this assignment is trying to set up visual studio code to make it compatible with everything. It was also the very first time I had ever touched circuit python, and the language was very different to what I was used to; Arduino language. 




## CircuitPython_Servo

### Description & Code

The purpose of this assignment is to make a servo move using the Adafruit metro board 

```python
import board                       #[1-16] Setup for Buttons                 
import time                        #And servo
import math
import pwmio 
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn2.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.pull = Pull.UP

pwm = pwmio.PWMOut(board.D5, duty_cycle=2 **15, frequency=50)
myServo = servo.Servo(pwm)

print("starting") 
while True:                 #[17-27]If a button is pressed
    print("re")             #Rotate to either 180 or 0
    if btn.value == True:
        myServo.angle = 180
        time.sleep(1)
        print("Right")
    elif btn2.value == True :
        myServo.angle = 0
        time.sleep(1)
        print("Left")
```

### Evidence

![name](https://github.com/aweder05/CircuitPython/blob/master/media/spinner.gif.gif?raw=true)

### Wiring

![name](https://github.com/aweder05/CircuitPython/blob/master/media/spinnerwiring.png?raw=true)

### Reflection

Adding a servo to the complexity of the code was a bit tricky, as the terminology was very different and new to me, but again, google came to help. The only tricky part really was having to move files from one lib folder to another, to allow the motor to actually spin. If I was to do this assignment again, I would definitely research servos more, to help with my knowledge of the functions of the motor. 



## CircuitPython_DistanceSensor

The purpose of this assignment is to turn the neopixel different colors corresponding to the distance measured on the HC-SR04 ultrasonic sensor. We want neopixel to turn red when your object is less than 5cm, blue when between 5 and 20cm, and green when farther than 20cm. Simultaneously, the distance is being printed on the serial monitor. 

### Description & Code

```python
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

```

### Evidence

![name](https://github.com/aweder05/CircuitPython/blob/master/media/sensorvid.gif.gif?raw=true)

### Wiring

![name](https://github.com/aweder05/CircuitPython/blob/master/media/sensorwiring.png?raw=true)

### Reflection

The process to complete this assignment was very much similar to the Servo assignment, where all I had to do was copy some code down into my Visual Studio Code app, mess around with some of the colors, and move some files from, again, one lib folder to another. One thing I would do differently would be to try some easier solutions to the code. I just feel like the code I was using was too long for it’s purpose. 




## LCD Backpack Button Counter with Toggle Feature

The purpose of this assignment was to wire two buttons and an LCD backpack to a breadboard. Each time pushing the button wired to the digital 3 pin, the counter on the LCD would increase by one. But, when holding down the button wired to the digital 2 pin, and then pressing the other button while holding down the first one, the counter would decrease by one. All of this is printed on the liquid crystal display (LCD) backpack.

### Description & Code

```python
import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object
i2c = board.I2C()
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
cur_state = True
prev_state = True
cur_state2 = True
prev_state2 = True
buttonPress = 0

while True:
    while btn2.value == False:
        cur_state = btn.value
        if cur_state != prev_state:
            if not cur_state:
                buttonPress = buttonPress + 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
        prev_state = cur_state
    else:
        cur_state2 = btn.value
        if cur_state2 != prev_state2:
            if not cur_state2:
                buttonPress = buttonPress - 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
        prev_state2 = cur_state2

```

### Evidence

![name](https://github.com/aweder05/CircuitPython/blob/master/media/lcdbuttontoggle.gif.gif?raw=true)

### Wiring

![name](https://github.com/aweder05/CircuitPython/blob/master/media/lcdbuttontogglewiring.png?raw=true)

### Reflection

This assignment was more difficult than the other three just because it took a while to nail down the wiring and to tweak around with the code.
