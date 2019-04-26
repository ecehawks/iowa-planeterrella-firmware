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
while (i != 60):
    air_pressure =  db.child("air_pressure").get().val()
    mode = db.child("mode").get().val()
    voltage = db.child("voltage_control").get().val()

    #########################
    # work done based on mode (5 GPIO)
    #
    # Current setup Little sphere is connected positive and negative
    # 1 & 7, 12 & 5, 11 & 6 are dead (off) postion
    # 2 & 8  = Top Needle, Big Sphere           Aurora
    # 3 & 9  = Second Needle, Little sphere-    Belts (auroral lobe)
    # 4 & 10 = Little sphere+, Big Sphere       Ring Current
    #########################
    if (mode == "Aurora"):
        db.child("ui-planeterrella").child("voltage").update("1")
        print ("%s" %mode)

    elif (mode == "Belt"):
        db.child("ui-planeterrella").child("voltage").update("50")
        print ("%s" %mode)

    elif (mode == "Ring"):
        db.child("ui-planeterrella").child("voltage").update("99")
        print ("%s" %mode)

    else:
        print ("Invalid mode type passed: %s " %(mode)) 

    #################################
    # Work done based on air_pressure
    #################################
    if (air_pressure == "Low"):
        db.child("ui-planeterrella").child("current").update("1")
        print ("%s\n" %air_pressure)

    elif (air_pressure == "Medium"):
        db.child("ui-planeterrella").child("current").update("50")
        print ("%s\n" %air_pressure)

    elif (air_pressure == "High"):
        db.child("ui-planeterrella").child("current").update("99")
        print ("%s\n" %air_pressure)
        
    else:
        print ("Invalid air_pressure type passed: %s" %(air_pressure))



    sleep(5)
    i += 1

