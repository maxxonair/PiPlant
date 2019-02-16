import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinList = [21, 26, 20, 16]

for i in pinList:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.LOW)

sleepTime=0.1

while True:
	for i in pinList:
        	GPIO.output(i, GPIO.HIGH)
        	time.sleep(sleepTime)

	for i in pinList:
		GPIO.output(i, GPIO.LOW)
		time.sleep(sleepTime)
