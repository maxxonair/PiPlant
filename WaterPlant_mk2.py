#---------------------------------------------------------------------------------------------------
#
#					Pi Water Plant Script
#
# Water plant script mk2
# Moisture feedback sensor data
# Motor is controlled using a timer
# One pump per plant / one water reservoir per plant
#---------------------------------------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
import datetime
import smtplib
import datetime



smtp_username = "apikey"
smtp_password = "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"
smtp_host = "smtp.sendgrid.net" 
smtp_port = 25
smtp_sender = "email@gmail.com"
smtp_receiver = "email@gmx.de" 

message_aloe = """From: Home PiPlant <email@gmail.com>
To: Max <email@gmx.de>
Subject: Home PiPlant need some water

Aloe needs water 
"""

message_palmi = """From: Home PiPlant <email@gmail.com>
To: Max <email@gmx.de>
Subject: Home PiPlant need some water

Palmi needs water 
"""

def sendEmail(email_message):
        try:
                smtpObj = smtplib.SMTP(smtp_host, smtp_port)
                smtpObj.login(smtp_username, smtp_password)
                smtpObj.sendmail(smtp_sender, smtp_receiver, email_message)
                print "notification mail sent" 
        except smtplib.SMTPException:
                print "ERROR: sending mail failed" 


WaitingTime_motorON=3
WaitingTime_motorOFF=10
channel_motor=21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print "Water plant mk2: RUN"
print "Date Time Aloe Palm"
# Pin list for motor actuators
pin_Motor = [21, 26, 20, 16]
# Pin list for moisture sensor input signal
pinList_Sensor = [2,          3]
#                Palm        Aloe

def Water_Plant(water_time, pin):
	# Water 
	print "Pump cmd: ON"
        GPIO.output(pin,GPIO.LOW)
        time.sleep(water_time)
        print "Pump cmd: OFF"
        GPIO.output(pin,GPIO.HIGH)
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
for i in pin_Motor:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

for i in pinList_Sensor:
	GPIO.setup(i, GPIO.IN)

mailsent_Aloe = False
mailsent_Palmi= False
# Main loop (endless)
while True:
	#--------------------------------------------------
	# Take moisture measurement:
	PALM  = Moisture_Measurement(0)
	ALOE  = Moisture_Measurement(1)
	currentDT = datetime.datetime.now()
	print ("%s %s %s" % (str(currentDT), ALOE, PALM))
	#--------------------------------------------------
	# Send notification :
	if (PALM ==1 or ALOE==1):
		if PALM==1 and mailsent_Palmi==False:
			#sendEmail(message_palmi)
			mailsent_Palmi=True
		if ALOE==1 and mailsent_Aloe==False:
			#sendEmail(message_aloe)
			mailsent_Aloe=True
	#-------------------------------------------------
	# Night time peace 
	now = datetime.datetime.now()
	if now.hour>8 and  now.hour<23:
		# Water plant:
		Watering_time = 1.1
		if PALM==1:
			Water_Plant(Watering_time,pin_Motor[3]) 
		if ALOE==1:
			Water_Plant(Watering_time,pin_Motor[2])
	#------------------------------------------------
	# Check reservoir water level
	# TBD
	#------------------------------------------------
	# Sleep for 15 minutes
        time.sleep(900)
print "Finish"
