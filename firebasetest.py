#import RPi.GPIO as GPIO
from time import sleep
import pyrebase
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)

#GPIO.setup(26, GPIO.OUT) #pwm pin 37 on pi
#p = GPIO.PWM(26, 100)
#p.start(0)

config = {
  "apiKey": "AIzaSyAkHCx7BgKyYlZgToo2hZgM2g61RrKZYcU",
  "authDomain": "ui-planeterrella.firebaseapp.com",
  "databaseURL": "https://ui-planeterrella.firebaseio.com/",
  "storageBucket": "ui-planeterrella.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

i=0
while (i != 10):
	air_pressure = 	db.child("air_pressure").get().val()
	mode = db.child("mode").get().val()
	voltage = db.child("voltage").get().val()

	#########################
	# work done based on mode
	#########################
	if (mode == "Aurora"):
		#gpio stuff
		print (mode)

	elif (mode == "Ring"):
		print (mode)

	elif (mode == "Belt"):
		print (mode)

	else:
		print ("\nInvalid mode type passed\n") 

	#################################
	# Work done based on air_pressure
	#################################
	if (air_pressure == "Low"):
		print (air_pressure)

	elif (air_pressure == "Medium"):
		print (air_pressure)

	elif (air_pressure == "High"):
		print (air_pressure)

	else:
		print ("\nInvalid air_pressure type passed\n") 

	
	################
	#voltage control
	#
	#will have to do some math to figure out relation between changing pwm frequenzy and voltage increment
	################

	#p.ChangeDutyCycle(voltage)



	sleep(0.5)
	i += 1