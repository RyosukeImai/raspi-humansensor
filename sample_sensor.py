import RPi.GPIO as GPIO
import time 

### setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN) # GPIO 18 : human detect sensor
#GPIO.setup(6, GPIO.OUT) # GPIO 6: LED

# initialize
#if GPIO.input(18):
#  GPIO.output(6, 1)
#else:
#  GPIO.output(6, 0)

while True:
    GPIO.wait_for_edge(18, GPIO.BOTH)
    if GPIO.input(18):
        print "detected!"
    #    GPIO.output(6, 1)
    else:
        print "non detected!"
    #    GPIO.output(6, 0)

    time.sleep(1)

GPIO.cleanup()

