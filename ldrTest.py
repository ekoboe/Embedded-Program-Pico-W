from machine import Pin,ADC
from utime import sleep


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
    
    print("Nilai Cahaya:", cahaya, "%")
   
    sleep(0.5)
