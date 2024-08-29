from machine import Pin, I2C
from bme_module import BME280Module
from utime import sleep
from ultrasonic import ULTRASONNIC
import utime
from ssd1306 import SSD1306_I2C

i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
widht = 128
height= 64
display = SSD1306_I2C(widht, height, i2c)

buzzer = Pin(5,Pin.OUT)

sda = Pin(0)
scl = Pin(1)
bme_module = BME280Module(0, scl, sda)
usonic = ULTRASONNIC(2,3)


while True:
    temp, pressure,humdt, altitude = bme_module.get_sensor_readings()
    jarak = usonic.ultrasonnic()

    print("============================")
    print("     SENSOR BME-280         ")
    print("----------------------------")
    print("Suhu         : ",temp)
    print("Tekanan Udara: ",pressure)
    print("Kelembahan   : ",humdt)
    print("Ketinggian   : ",altitude)
    print("----------------------------")
    
    print("============================")
    print("     SENSOR HSRF-05         ")
    print("----------------------------")
    print("Jarak        :",jarak)
    print("----------------------------")

    if temp >= 28:
        print("**********")
        stsBz = "ON"
        buzzer.on()
        print(" Alarm ON ")
        print("**********")
        
    elif jarak <= 25:
        print("**********")
        stsBz = "ON"
        buzzer.on()
        print(" Alarm ON ")
        print("**********")
        
    elif altitude >= 900:
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
    display.text('Temp  : ',0, 18, 1)
    display.text(str(temp),63, 18, 1)
    display.text('Jarak : ',0, 28, 1)
    display.text(str(jarak),63, 28, 1)
    display.text('ALt   : ',0, 38, 1)
    display.text(str(altitude),63, 38, 1)
    display.text('Status: ',0, 53, 1)
    display.text(stsBz,63, 53, 1)
    display.hline(0, 63, 127, 1)
    display.hline(0, 0, 127, 1)
    display.hline(0, 14, 127, 1)
    display.hline(0, 50, 127, 1)
    display.vline(0, 0, 63, 1)
    display.vline(127, 0, 63, 1)
    display.show()
    
    sleep(1)
    