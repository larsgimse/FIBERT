from serial import Serial
from time import sleep

microbitPort = '/dev/tty.usbmodem1412' # USB port address for the micro:bit /dev/ttyACM0 or /dev/tty.usbmodem40132 or similar
microbitBaud = '115200' # Baud for serial communication

ser = Serial(microbitPort, microbitBaud, timeout=3)

while True:
    trigger = input("trigger: ")
    ser.write(str.encode(trigger + "\n"))
    print(trigger)
    sleep(1)
