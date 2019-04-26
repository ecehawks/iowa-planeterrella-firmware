from time import sleep
import pyrebase



config = {
  "apiKey": "AIzaSyAkHCx7BgKyYlZgToo2hZgM2g61RrKZYcU",
  "authDomain": "ui-planeterrella.firebaseapp.com",
  "databaseURL": "https://ui-planeterrella.firebaseio.com/",
  "storageBucket": "ui-planeterrella.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

i=0
while (i != 5):
    air_pressure =  db.child("air_pressure").get().val()
    mode = db.child("mode").get().val()
    voltage = db.child("voltage_control").get().val()

    db.update({"voltage": "50"})

    voltcheck = db.child("voltage").get().val()
    print(voltcheck)


    sleep(5)
    i += 1

db.update({"voltage": "0"})