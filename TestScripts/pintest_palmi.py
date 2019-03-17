import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinList = [21, 26, 20, 16]


GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.LOW)
time.sleep(0.5)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.HIGH)

