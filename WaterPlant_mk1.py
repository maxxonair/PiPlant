# Water plant script mk1
# No feedback (sensor data)
# Motor is controlled using a timer

import RPi.GPIO as GPIO
import time

WaitingTime_motorON=3
WaitingTime_motorOFF=10
channel_motor=21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
print "Water plant mk1: RUN"

pinList = [21, 26, 20, 16]

# Set all Pump pins to high (switch off)
for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

% Main loop (endless)
while True:
	# Water 
        print "Pump on"
        GPIO.output(21,GPIO.LOW)
        time.sleep(3)
        print "Pump off"
        GPIO.output(21,GPIO.HIGH)
        time.sleep(300)
	# Take moisture measurement
print "Finish"
