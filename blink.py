import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
i=0
while (i<10):
    GPIO.output(40, GPIO.HIGH)
    sleep(1)
    GPIO.output(40, GPIO.LOW)
    sleep(1)
    i+=2
    
GPIO.output(40, GPIO.LOW)