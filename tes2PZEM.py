from pzem import PZEM
from machine import Pin, I2C, ADC, UART
import time

uart = UART(0, baudrate=9600)
dev = PZEM(uart=uart)

def pzem1():
    if dev.read():
        tegangan = round(dev.getVoltage())
        arus = round(dev.getCurrent(), 2)
        daya = dev.getActivePower()
        return tegangan, arus, daya

while True:
    v,i,w = pzem1()
    print("Voltage : ", v)
    print("Arus : ", i)
    print("Daya : ", w)
    
    time.sleep(1)

