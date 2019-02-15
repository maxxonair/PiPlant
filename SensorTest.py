import RPi.GPIO as GPIO
import time

#GPIO setup
channel = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
	if GPIO.input(channel):
		print("no water detected")
	else:
		print("water detected")

#GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
#GPIO.add_event_callback(channel, callback)

#infinite loop 
while True:
	sensor_01_value= GPIO.input(channel)
	print sensor_01_value
	time.sleep(.1)

