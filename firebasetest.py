import RPi.GPIO as GPIO
from time import sleep
import pyrebase



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(20, GPIO.OUt, initial=GPIO.LOW)
GPIO.setup(20, GPIO.OUt, initial=GPIO.LOW)
GPIO.setup(20, GPIO.OUt, initial=GPIO.LOW)


config = {
  "apiKey": "AIzaSyAkHCx7BgKyYlZgToo2hZgM2g61RrKZYcU",
  "authDomain": "ui-planeterrella.firebaseapp.com",
  "databaseURL": "https://ui-planeterrella.firebaseio.com/",
  "storageBucket": "ui-planeterrella.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


i=0
while (1):
	db.update({"voltage": testingpos})
	if PRGM:
		print ("IRPGM_pos = ", IPRGM_Pos)
	else:
		print ("ERPGM_pos = ", EPRGM_Pos)

	sleep(1)
	i +=1



