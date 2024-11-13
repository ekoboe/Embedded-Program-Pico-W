from pzem import PZEM
import machine
import time

sleep = 3 * 1000

uart = machine.UART(0, baudrate=9600)

# define PZEM device [UART, ADDR = 0xF8 (default)]
dev = PZEM(uart=uart)

# Set new address
if dev.setAddress(0x05):
    print("New device address is {}".format(dev.getAddress()))

# Buzzer configuration
buzzer_pin = machine.Pin(16, machine.Pin.OUT)  # Assuming buzzer is connected to GPIO pin 16

def activate_buzzer():
    buzzer_pin.on()
    time.sleep(1)  # Buzzer activation duration
    buzzer_pin.off()

while True:
    # Read the new values
    if dev.read():
        # Print the reading values (public fields)
        #print("Current:", dev.getCurrent())  # Modified line to include current reading
        #print("Voltage:", dev.getVoltage())
        #print("Active Power:", dev.getActivePower())
        print("Active Energy:", dev.getActiveEnergy())
        print("reset actived!", dev.resetEnergy())
        
        # Activate the buzzer
        #activate_buzzer()

    # Wait for the next reading
    time.sleep_ms(sleep - dev.getReadingTime())
