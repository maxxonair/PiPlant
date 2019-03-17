import RPi.GPIO as GPIO
import time
import datetime
import smtplib


smtp_username = "apikey"
smtp_password = "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"
smtp_host = "smtp.sendgrid.net" 
smtp_port = 25
smtp_sender = "maxbr4un@gmail.com"
smtp_receiver = "maxx2x@gmx.de" 

message_aloe = """From: Home PiPlant <maxbr4un@gmail.com>
To: Max <maxx2x@gmx.de>
Subject: Home PiPlant need some water

Aloe needs water 
"""

message_palmi = """From: Home PiPlant <maxbr4un@gmail.com>
To: Max <maxx2x@gmx.de>
Subject: Home PiPlant need some water

Palmi needs water 
"""

message = """From: Home PiPlant <maxbr4un@gmail.com>
To: Max <maxx2x@gmx.de>
Subject: Home PiPlant need some water

Aloe and Palmi need water 
"""


def sendEmail(email_message):
	try:
		smtpObj = smtplib.SMTP(smtp_host, smtp_port)
		smtpObj.login(smtp_username, smtp_password)
		smtpObj.sendmail(smtp_sender, smtp_receiver, email_message)
		print "sending mail successful" 
	except smtplib.SMTPException:
		print "ERROR: sending mail failed" 


sendEmail(message)


