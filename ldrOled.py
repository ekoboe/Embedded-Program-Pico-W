from machine import Pin,ADC, I2C
from utime import sleep
from ssd1306 import SSD1306_I2C

i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
widht = 128
height= 64
display = SSD1306_I2C(widht, height, i2c)

pinLDR = ADC(26)
buzzer = Pin(5,Pin.OUT)
lamp = Pin(9,Pin.OUT)
suhu = ADC(4)

while True:
    nilaiADC = suhu.read_u16()
    voltage = nilaiADC * (3.3 / 65535.0)
    celcius = round(27 - (voltage - 0.706) / 0.001721,2)
    fahrenheit = celcius * (9/5) + 32
    
    dataLDR = pinLDR.read_u16()
    cahaya = round((dataLDR/(65535.0))*100,2)
    print("Internal Temperature:", celcius, "°C")
    print("Internal Temperature:", fahrenheit, "°F")

    print(cahaya)
    
    if cahaya >= 30:
        print("**********")
        stsBz = "OFF"
        stsLmp = "OFF"
        buzzer.off()
        lamp.off()
        print(" Alarm OFF ")
        print("**********")
    else:
        print("**********")
        stsBz = "ON"
        stsLmp ="ON"
        buzzer.on()
        lamp.on()
        print(" Alarm ON ")
        print("**********")
    
    display.fill(0)    
    display.text('MONITORING',23, 3, 1)
    display.text('Temp  : ',0, 18, 1)
    display.text(str(celcius),63, 18, 1)
    display.text('LDR   : ',0, 28, 1)
    display.text(str(cahaya),63, 28, 1)
    display.text('Buzz  : ',0, 42, 1)
    display.text(str(stsBz),63, 42, 1)
    display.text('Lamp  : ',0, 53, 1)
    display.text(stsLmp,63, 53, 1)
    display.hline(0, 63, 127, 1)
    display.hline(0, 0, 127, 1)
    display.hline(0, 14, 127, 1)
    display.hline(0, 39, 127, 1)
    display.vline(0, 0, 63, 1)
    display.vline(127, 0, 63, 1)
    display.show()
    
    sleep(0.5)
