# CircuitPython

## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
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
#SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 10):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -10): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
```

### Evidence

![name](https://github.com/aweder05/CircuitPython/blob/master/media/spinnervid.gif.gif?raw=true)

### Wiring

![name](https://github.com/aweder05/CircuitPython/blob/master/media/spinnerwiring.png?raw=true)

### Reflection

Adding a servo to the complexity of the code was a bit tricky, as the terminology was very different and new to me, but again, google came to help. The only tricky part really was having to move files from one lib folder to another, to allow the motor to actually spin. If I was to do this assignment again, I would definitely research servos more, to help with my knowledge of the functions of the motor. 



## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence



### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
