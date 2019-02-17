import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)


pinList = [21, 26, 20, 16]

for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)

while True:
	print "Motor on"
	GPIO.output(16,GPIO.HIGH)
	time.sleep(2)
	print "Motor off" 
	GPIO.output(16,GPIO.LOW)
	time.sleep(15)
print "Finish"
