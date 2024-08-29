from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from ultrasonic import ULTRASONNIC
from utime import sleep

usonic = ULTRASONNIC(2,3)
i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
display = SSD1306_I2C(128, 64, i2c)
buzzer = Pin(5, Pin.OUT)
buzzer.off()


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
    
    display.fill(0)    
    display.text('MONITORING',23, 3, 1)
    display.text('Jarak  : ',0, 18, 1)
    display.text(str(jarak),63, 18, 1)
    display.text('Status :',0, 53, 1)
    display.text(stsBz,63, 53, 1)
    display.hline(0, 63, 127, 1)
    display.hline(0, 0, 127, 1)
    display.hline(0, 14, 127, 1)
    display.hline(0, 50, 127, 1)
    display.vline(0, 0, 63, 1)
    display.vline(127, 0, 63, 1)
    display.show()

    sleep(1)