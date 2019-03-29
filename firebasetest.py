#import RPi.GPIO as GPIO
from time import sleep
import pyrebase
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)

####### Setup gpio pins for mode configuration #########
# GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)  # Second Needle
# GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)  # Top Needle
# GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) # Little Sphere (Pos)
# GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) # Little Sphere (Neg)
# GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # Big Sphere

##### PWM Setup #############
#GPIO.setup(21, GPIO.OUT) #pwm pin 40 on pi
#p = GPIO.PWM(21, 100)
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
	# work done based on mode (5 GPIO)
	#
	# Current setup Little sphere is connected positive and negative
	# 1 & 7, 12 & 5, 11 & 6 are dead (off) postion
	# 2 & 8  = Top Needle, Big Sphere   		Aurora
	# 3 & 9  = Second Needle, Little sphere- 	Belts (auroral lobe)
	# 4 & 10 = Little sphere+, Big Sphere 		Ring Current
	#########################
	if (mode == "Aurora"):
		#gpio stuff
		# GPIO.output(5, GPIO.LOW)
		# GPIO.output(6, GPIO.HIGH)
		# GPIO.output(13, GPIO.LOW)
		# GPIO.output(19, GPIO.LOW)
		# GPIO.output(26, GPIO.HIGH)
		print (mode)

	elif (mode == "Belt"):
		# GPIO.output(5, GPIO.LOW)
		# GPIO.output(6, GPIO.HIGH)
		# GPIO.output(13, GPIO.LOW)
		# GPIO.output(19, GPIO.HIGH)
		# GPIO.output(26, GPIO.LOW)
		print (mode)

	elif (mode == "Ring"):
		# GPIO.output(5, GPIO.LOW)
		# GPIO.output(6, GPIO.LOW)
		# GPIO.output(13, GPIO.HIGH)
		# GPIO.output(19, GPIO.LOW)
		# GPIO.output(26, GPIO.HIGH)
		print (mode)

	else:
		print ("Invalid mode type passed: %s " %(mode)) 

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
		print ("Invalid air_pressure type passed: %s" %(air_pressure)) 

	
	################
	#voltage control
	#
	#will have to do some math to figure out relation between changing pwm frequenzy and voltage increment
	################

	#p.ChangeDutyCycle(voltage)



	sleep(0.5)
	i += 1