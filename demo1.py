

import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BUTTON=10
GPIO.setup(BUTTON, GPIO.IN)

LDR=11
GPIO.setup(LDR,GPIO.IN)

LED=17
GPIO.setup(LED,GPIO.OUT)

BUZZER=22
GPIO.setup(BUZZER,GPIO.OUT)


		
def idLED(second,number):
	duration=second/number/2
	
	for i in range(number):
		
		GPIO.output(LED,GPIO.HIGH)
		time.sleep(duration)		

		GPIO.output(17,GPIO.LOW)
		time.sleep(duration)

def fifteen():
	idLED(10.0,10)
	for i in range(10):
		idLED(1.0,(i+1)*2)

def buzzer (second):
	for i in range(second*5):
		GPIO.output(22,GPIO.HIGH)
		time.sleep(.1)
		GPIO.output(22,GPIO.LOW)
		time.sleep(.1)

def RCtime (RCpin):
	reading = 0
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
	time.sleep(.1) 
	GPIO.setup(RCpin, GPIO.IN)
	while (GPIO.input(RCpin) == GPIO.LOW):
		reading += 1 
	return reading
	

while True:
        if ( GPIO.input(10) == False ):
                os.system('date')
                print("Button is pressed.")
                print("The last number in id is 8.")
                idLED(5.0,8)
		print("Count 15 seconds.")
                fifteen()
                buzzer(3)

                while True:
                        if RCtime(LDR)>300:
                                GPIO.output(LED,GPIO.HIGH)

        else:
                os.system('clear')
                print ("press the button..")

