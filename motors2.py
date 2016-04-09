import RPi.GPIO as GPIO
import time
import curses

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

def exit():
    turn_off_motors()
    curses.endwin()
    GPIO.cleanup()

print("Control robot with arrow keys, press Q to quit.\n")
screen = curses.initscr()
curses.cbreak()
screen.keypad(1)
key = ''

while True:
    key = screen.getch()

    if key == curses.KEY_UP:
        forward()
        time.sleep(0.1)
    elif key == curses.KEY_DOWN:
        backward()
        time.sleep(0.1)
    elif key == curses.KEY_LEFT:
        left()
        time.sleep(0.1)
    elif key == curses.KEY_RIGHT:
        right()
        time.sleep(0.1)
    elif key == ord('s'):
        turn_off_motors()
    elif key == ord('q'):
        break
    turn_off_motors()
    
#reset and turn off motors
exit()
