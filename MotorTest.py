import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
print "Motor on"
GPIO.output(21,GPIO.HIGH)
time.sleep(3)
print "Motor off" 
GPIO.output(21,GPIO.LOW)
print "Finish"
