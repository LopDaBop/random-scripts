import RPi.GPIO as GPIO  ### import module that controls the GPIO pins on the Raspberry Pi
import time  ### importing the time library, [useful for adding delays]

### These are the pins for the L298N motor driver
IN1 = 17  ### Pin 17 for motor control [i think its forward]
IN2 = 18  ### Pin 18 for motor control 2 [backwards]
ENA = 22  ### Pin 22 for motor enable [not needed for now but could be used for speed control with PWM later on ig]

# setting up the GPIO pins
GPIO.setmode(GPIO.BCM)  ###Sets the Raspberry Pi pin numbering to Broadcom mode
GPIO.setup(IN1, GPIO.OUT)  ### Sets IN1 as an output pin, meaning we can send signals to this pin to control the motor
GPIO.setup(IN2, GPIO.OUT)  ### Sets IN2 as an output pin to control the other direction of the motor
GPIO.setup(ENA, GPIO.OUT)  ### Sets ENA as an output pin, which we may use later for speed control

def motor_forward():
    GPIO.output(IN1, GPIO.HIGH)  ### Sets IN1 to HIGH, which should contribuite to going straihgt
    GPIO.output(IN2, GPIO.LOW)   ### Sets IN2 to LOW, completing the circuit and powering the motor

def motor_backward():
    GPIO.output(IN1, GPIO.LOW)   ### Sets IN1 to LOW, turning the motor in the opposite direction [bckwards]
    GPIO.output(IN2, GPIO.HIGH)  ### Sets IN2 to HIGH, completing the circuit to power the motor in reverse

def motor_stop():
    GPIO.output(IN1, GPIO.LOW)   ### Sets both IN1 and IN2 to LOW, cutting off power to the motor (motor stops)
    GPIO.output(IN2, GPIO.LOW)   ### Stops the motor by not allowing current to flow through it



#### Test the DC motor

###Move motor forward
motor_forward()
time.sleep(2)

###Move motor back
motor_backward()
time.sleep(2)

##Stop motor
motor_stop()
time.sleep(2)



##apparently you can use GPIO.cleanup() to reset the GPIO pins to their default state [stole this from sherkhan xd]
GPIO.cleanup()  ### This is will avoid any weird behavior when you run the program again
