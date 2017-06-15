#按下 Push Button 後啟動溫度感測器。當
#溫度感測器超過指定溫度（請自訂）時
#蜂鳴器響起。此如如果 PIR 連續偵測
#三次motion，則蜂鳴器停止作響。Buzzer
#的鳴叫頻率可以自設。
#"(加分)請利用 Push Button、Buzzer、PIR、LED 等設計一個小專題。

import os
import glob
import time

#initialize the device
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines
def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		temp_f = temp_c * 9.0 / 5.0 + 32.0
 		return temp_c, temp_f

#不停做溫度偵測
while True:
	count=0
	print(read_temp())


	#溫度超過五十度
	if read_temp()>50:
		while True:
			if()
			buzzer()				
	time.sleep(1)
	 
def buzzer ():
	for i in range (5):
		GPIO.output(22,GPIO.HIGH)
		time.sleep(.1)
		GPIO.output(22,GPIO.LOW)
		time.sleep(.1)
