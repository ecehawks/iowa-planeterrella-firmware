import RPi.GPIO as GPIO
from time import sleep
from firebase import firebase

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
firebase = firebase.FirebaseApplication('https://ui-planeterrella.firebaseio.com/', None)


i=0
while (i < 50):
	result = firebase.get('/led_On', None)
	print (result)

	if result:
	    GPIO.output(40, GPIO.HIGH)
	else:
	    GPIO.output(40, GPIO.LOW)
	i += 1
	sleep(1)

GPIO.output(40, GPIO.LOW)

