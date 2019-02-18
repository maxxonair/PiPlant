
# Water plant script mk1
# No feedback (sensor data)
# Motor is controlled using a timer

import RPi.GPIO as GPIO
import time
import datetime

WaitingTime_motorON=3
WaitingTime_motorOFF=10
channel_motor=21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print "Water plant mk1: RUN"
print "Date Time Aloe Palm"
# Pin list for motor actuators
pinList = [21, 26, 20, 16]
# Pin list for moisture sensor input signal
pinList_Sensor = [2,          3]
#                Palm        Aloe

def Water_Plant(water_time):
	# Water 
	print "Pump cmd: ON"
        GPIO.output(21,GPIO.LOW)
        time.sleep(water_time)
        print "Pump cmd: OFF"
        GPIO.output(21,GPIO.HIGH)
WET="WET"
DRY="DRY"

def Moisture_Measurement(Sensor):
	# Take Moisture Measurement
	if GPIO.input(pinList_Sensor[Sensor])==0:
		#print "Sensor reading: WET"
		return 0
	else: 
		#print "Sensor reading: DRY"
		return 1

# Set all Pump pins to high (switch off)
for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

for i in pinList_Sensor:
	GPIO.setup(i, GPIO.IN)

# Main loop (endless)
while True:
	# Take moisture measurement:
	PALM  = Moisture_Measurement(0)
	ALOE  = Moisture_Measurement(1)
	currentDT = datetime.datetime.now()
	print ("%s %s %s" % (str(currentDT), ALOE, PALM))
	#print ("Aloe: ", ALOE)
	#print ("Palm: ", PALM)
	# Sleep for 15 minutes
        time.sleep(900)
print "Finish"
