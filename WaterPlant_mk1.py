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

while True:
	print "Motor on"
	GPIO.output(channel_motor,GPIO.HIGH)
	time.sleep(WaitingTime_motorON)
	GPIO.output(channel_motor,GPIO.LOW)
	print "Motor off"
	time.sleep(WaitingTime_motorOFF)
