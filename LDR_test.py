from machine import ADC, Pin
import time

ldr = ADC(Pin(26))  # GP26 is ADC0

def read_ldr():
    # Read the LDR value, which will be between 0 and 65535 on a 16-bit scale
    light_value = ldr.read_u16()
    return light_value

while True:
    # Read and print the LDR value
    light_value = read_ldr()
    print("Light level:", light_value)
    time.sleep(1)
