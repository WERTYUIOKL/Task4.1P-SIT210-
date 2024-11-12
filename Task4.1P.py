import RPi.GPIO as GPIO
import time

# Set up the GPIO mode and pin
GPIO.setmode(GPIO.BCM)  
GPIO.setup(18, GPIO.OUT)  

try:
    while True:
        GPIO.output(18, GPIO.HIGH)  # Turn on LED
        time.sleep(1)              # Wait for 1 second
        GPIO.output(18, GPIO.LOW)   # Turn off LED
        time.sleep(1)              # Wait for 1 second
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up all GPIO states on exit
