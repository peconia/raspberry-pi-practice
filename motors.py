import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

leftBackward = 7
leftForward = 8
rightBackward = 9
rightForward = 10

# set pin mode
GPIO.setup(leftBackward, GPIO.OUT)
GPIO.setup(leftForward, GPIO.OUT)
GPIO.setup(rightBackward, GPIO.OUT)
GPIO.setup(rightForward, GPIO.OUT)

def turn_off_motors():
    GPIO.output(leftBackward, 0)
    GPIO.output(leftForward, 0)
    GPIO.output(rightBackward, 0)
    GPIO.output(rightForward, 0)

def forward():
    GPIO.output(leftBackward, 0)
    GPIO.output(leftForward, 1)
    GPIO.output(rightBackward, 0)
    GPIO.output(rightForward, 1)

def backward():
    GPIO.output(leftBackward, 1)
    GPIO.output(leftForward, 0)
    GPIO.output(rightBackward, 1)
    GPIO.output(rightForward, 0)

def left():
    GPIO.output(leftBackward, 1)
    GPIO.output(leftForward, 0)
    GPIO.output(rightBackward, 0)
    GPIO.output(rightForward, 1)

def right():
    GPIO.output(leftBackward, 0)
    GPIO.output(leftForward, 1)
    GPIO.output(rightBackward, 1)
    GPIO.output(rightForward, 0)

turn_off_motors()
forward()
time.sleep(1)
left()
time.sleep(0.5)
backward()
time.sleep(0.5)
right()
time.sleep(0.5)

#reset and turn off motors
GPIO.cleanup()
