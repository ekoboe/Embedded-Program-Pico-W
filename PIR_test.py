from machine import Pin
import time


pir = Pin(15, Pin.IN)  # GP15 sebagai input dari sensor PIR

while True:
    if pir.value() == 1:
        print("Gerakan terdeteksi!")
    else:
        print("Tidak ada gerakan.")
    
    time.sleep(1)
