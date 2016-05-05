import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)  # pan
GPIO.setup(16, GPIO.OUT)  # tilt

pan_pin = GPIO.PWM(12, 50)
pan_pin.start(7.5)

tilt_pin = GPIO.PWM(16, 50)
tilt_pin.start(7.5)

try:
    while True:
        pan_pin.ChangeDutyCycle(12.5) # 180 degrees, card this side!
        time.sleep(0.5)
        pan_pin.ChangeDutyCycle(0)
        tilt_pin.ChangeDutyCycle(11) # down
        time.sleep(0.5)
        tilt_pin.ChangeDutyCycle(0)
        time.sleep(3)  # wait for card to be read

        tilt_pin.ChangeDutyCycle(5) # up
        time.sleep(0.5)
        tilt_pin.ChangeDutyCycle(0)
        pan_pin.ChangeDutyCycle(0.1) # 0 degrees
        time.sleep(0.5)
        pan_pin.ChangeDutyCycle(0)
        time.sleep(1)


except KeyboardInterrupt:
    pan_pin.stop()
    tilt_pin.stop()
    GPIO.cleanup()

