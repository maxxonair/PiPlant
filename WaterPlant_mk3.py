#---------------------------------------------------------------------------------------------------
#
#					Pi Water Plant Script
#
# Water plant script mk3
# -> NO Moisture feedback sensor data
# Pumps are controlled only by using a timer
# One pump per plant / one water reservoir per plant
#---------------------------------------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
import datetime
import smtplib
import datetime


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print "Water plant mk3: RUN"
# Pin list for motor actuators
pin_Motor = [21, 26, 20, 16]

def Water_Plant(water_time, pin):
	# Water 
	print ("Pump %s cmd: ON" % (str(pin)))
        GPIO.output(pin,GPIO.LOW)
        time.sleep(water_time)
        print ("Pump %s cmd: OFF" % (str(pin)))
        GPIO.output(pin,GPIO.HIGH)


# Set all Pump pins to high (switch off)
for i in pin_Motor:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

# Main loop (endless)
while True:
	#--------------------------------------------------
	currentDT = datetime.datetime.now()
	#--------------------------------------------------
	# Night time peace 
	now = datetime.datetime.now()
	if now.hour>7 and  now.hour<23:
		# Water plant:
		Watering_time = 1.1
		if now.hour == 8  and now.minute < 15 :
			Water_Plant(Watering_time,pin_Motor[3])
			time.sleep(Watering_time)
			Water_Plant(Watering_time,pin_Motor[2]) 
			print ("%s %s Plants watered - morning" % (str(now.hour), str(now.minute)))
		if now.hour == 21 and now.minute < 15 :
			Water_Plant(Watering_time,pin_Motor[3])
			time.sleep(Watering_time)
			Water_Plant(Watering_time,pin_Motor[2])
			print ("%s %s Plants watered - evening" % (str(now.hour), str(now.minute)))
	#------------------------------------------------
	# Check reservoir water level
	# TBD
	#------------------------------------------------
	# Sleep for 15 minutes
        time.sleep(900)
print "Finish"
