import RPi.GPIO as GPIO
import time
import curses

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set up pins
leftBackward = 7
leftForward = 8
rightBackward = 9
rightForward = 10
pinTrigger = 17
pinEcho = 18

# set pin mode
GPIO.setup(leftBackward, GPIO.OUT)
GPIO.setup(leftForward, GPIO.OUT)
GPIO.setup(rightBackward, GPIO.OUT)
GPIO.setup(rightForward, GPIO.OUT)
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

# settings for motor speed
frequency = 20  # how many on/off per sec
duty_cycle = 30  # % how long pin stays on during cycle
stop = 0  # motors will not turn

# set pulse-width modulation
pwm_left_backward = GPIO.PWM(leftBackward, frequency)
pwm_left_forward = GPIO.PWM(leftForward, frequency)
pwm_right_backward = GPIO.PWM(rightBackward, frequency)
pwm_right_forward = GPIO.PWM(rightForward, frequency)

def start_pwm():
    pwm_left_backward.start(stop)  # initilaise not moving
    pwm_left_forward.start(stop)
    pwm_right_backward.start(stop)
    pwm_right_forward.start(stop)

def turn_off_motors():
    pwm_left_backward.ChangeDutyCycle(stop)
    pwm_left_forward.ChangeDutyCycle(stop)
    pwm_right_backward.ChangeDutyCycle(stop)
    pwm_right_forward.ChangeDutyCycle(stop)

def forward():
    pwm_left_backward.ChangeDutyCycle(stop)
    pwm_left_forward.ChangeDutyCycle(duty_cycle)
    pwm_right_backward.ChangeDutyCycle(stop)
    pwm_right_forward.ChangeDutyCycle(duty_cycle)

def backward():
    pwm_left_backward.ChangeDutyCycle(duty_cycle)
    pwm_left_forward.ChangeDutyCycle(stop)
    pwm_right_backward.ChangeDutyCycle(duty_cycle)
    pwm_right_forward.ChangeDutyCycle(stop)

def left():
    pwm_left_backward.ChangeDutyCycle(duty_cycle)
    pwm_left_forward.ChangeDutyCycle(stop)
    pwm_right_backward.ChangeDutyCycle(stop)
    pwm_right_forward.ChangeDutyCycle(duty_cycle)

def right():
    pwm_left_backward.ChangeDutyCycle(stop)
    pwm_left_forward.ChangeDutyCycle(duty_cycle)
    pwm_right_backward.ChangeDutyCycle(duty_cycle)
    pwm_right_forward.ChangeDutyCycle(stop)

def exit():
    turn_off_motors()
    curses.endwin()
    GPIO.cleanup()

def check_distance():
    GPIO.output(pinTrigger, 0)
    time.sleep(0.1)  # allow to settle
    # send pulse to trigger
    GPIO.output(pinTrigger, 1)
    time.sleep(0.00001) # 10 us
    GPIO.output(pinTrigger, 0)
    start_time = time.time()
    # reset start time until echo is taken high
    while GPIO.input(pinEcho) == 0:
        start_time = time.time()

    # stop when echo pin is no longer high
    while GPIO.input(pinEcho) == 1:
        stop_time = time.time()
        if stop_time - start_time >= 0.04:
            stop_time = start_time
            break

    elapsed_time = stop_time - start_time
    distance = elapsed_time *34326 / 2  # in cm
    return distance

def too_close():
    return check_distance() < 10

start_pwm()
print("Control robot with arrow keys, press Q to quit.\n")
screen = curses.initscr()
curses.cbreak()
screen.keypad(1)
key = ''

while True:
    key = screen.getch()

    if key == curses.KEY_UP:
        if not too_close():
            forward()
        else:
            right()  # turn right if too close to something
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
    
#reset and turn off motors
exit()
