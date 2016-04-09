import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinTrigger = 17
pinEcho = 18

GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

try:
    while True:
        GPIO.output(pinTrigger, 0)
        time.sleep(0.5)  # allow to settle
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
                print("Too close!")
                stop_time = start_time
                break

        elapsed_time = stop_time - start_time
        distance = elapsed_time *34326 / 2  # in cm
        print("distance %f cm" % distance)
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
        
