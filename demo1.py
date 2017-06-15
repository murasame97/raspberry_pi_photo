#按下 Push Button 後五秒開始閃爍 LED 燈號 n 次(n 是學號最後一碼)。
#倒數計時15秒，最後5秒 LED 燈號愈閃愈快。
#15 秒時間到後，LED 燈滅、Buzzer 啟動。
#如果光敏電阻LDR 暗，則點亮 LED。 
#Buzzer 的鳴叫頻率可以自設。


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#Button接到下排第十個
BUTTON=10
GPIO.setup(BUTTON, GPIO.IN)

#光敏電阻接到下排第十二個
LDR=11
GPIO.setup(LDR,GPIO.IN)

#LED接到下排第六個
LED=17
GPIO.setup(LED,GPIO.OUT)

#蜂鳴器接到下排第八個
BUZZER=22
GPIO.setup(BUZZER,GPIO.OUT)

#判斷Button甚麼時候被按下
while True:
	#按了
	if ( GPIO.input(10) == False ):
                #印出時間
		os.system('date')
		print("Button is pressed.")
				
		#五秒內顯示完學號
		print("The last number in id is 8.")
		idLED(5.0,8.0)
		
		#十五秒倒計時
		print("Count 15 seconds.")
		fifteen()
		
		#蜂鳴器警報三秒
		buzzer(3)
		
		#看光敏電阻有沒有被暗著
		while True:
			if RCtime(LDR)>300
				GPIO.output(LED,GPIO.HIGH)	
			
	#沒按
	else:
		os.system('clear')
		print ("press the button..")

#傳入秒數與亮燈次數
def idLED(second,number):
	#設定亮暗間隔
	duration=second/number/2
	
	for i in range(number):
		
		#Turn LEDs on
		GPIO.output(LED,GPIO.HIGH)
		time.sleep(duration)		

		#Turn LEDs off
		GPIO.output(17,GPIO.LOW)
		time.sleep(duration)

#倒數十五秒
def fifteen():
	#前十秒正常的數
	idLED(10,10)
	
	#後五秒越跑越快
	for i in range(10):
		idLED(1.0,i*2)

def buzzer (second):
	for i in range(second*5):
		#Dot Dot Dot
		GPIO.output(22,GPIO.HIGH)
		time.sleep(.1)
		GPIO.output(22,GPIO.LOW)
		time.sleep(.1)

#看光敏電阻讓電容充放的時間
#暗時較久
def RCtime (RCpin):
	reading = 0
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
	time.sleep(.1) GPIO.setup(RCpin, GPIO.IN)
	while (GPIO.input(RCpin) == GPIO.LOW):
		reading += 1 
	return reading
