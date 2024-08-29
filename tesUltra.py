from machine import Pin
from ultrasonic import ULTRASONNIC
from utime import sleep

buzzer = Pin(5, Pin.OUT)
buzzer.off()
usonic = ULTRASONNIC(2,3)

while True:    
    jarak = usonic.ultrasonnic()
    
    print("============================")
    print("     SENSOR HSRF-05         ")
    print("----------------------------")
    print("Jarak        :",jarak)
    print("----------------------------")
    
    if jarak <= 25:
        print("**********")
        stsBz = "ON"
        buzzer.on()
        print(" Alarm ON ")
        print("**********")
    else:
        print("**********")
        stsBz = "OFF"
        buzzer.off()
        print(" Alarm OFF ")
        print("**********")
  
    sleep(0.5)