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
print "Water plant mk1: RUN"

# Pin list for motor actuators
pinList = [21, 26, 20, 16]
# Pin list for moisture sensor input signal
pinList_Sensor = [2]

def Water_Plant(water_time):
	# Water 
	print "Pump cmd: ON"
        GPIO.output(21,GPIO.LOW)
        time.sleep(water_time)
        print "Pump cmd: OFF"
        GPIO.output(21,GPIO.HIGH)

def Moisture_Measurement(Sensor):
	# Take Moisture Measurement
	if GPIO.input(pinList_Sensor[Sensor])==0:
		print "Sensor reading: DRY"
		return True
	else: 
		print "Sensor reading: WET"
		return False

# Set all Pump pins to high (switch off)
for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

for i in pinList_Sensor:
	GPIO.setup(i, GPIO.IN)

# Main loop (endless)
while True:
	# Take moisture measurement:
	if  Moisture_Measurement(0):
		# Water 
        	Water_Plant(3)
	# Sleep for 10 minutes
        time.sleep(600)
print "Finish"
