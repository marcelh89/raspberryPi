# simple receiver python script for jeelink 868mhz frequency

# the signal should look like this
# OK 9 8 1 4 157 106

# whereas the integers mean the following
# 1. battery level: OK or Low
# 2. checksum: should be 9
# 3. address (changes with battery)
# 4.5. battery changing?!)
# 6. temperature: displayed as integer so 15,7 degree is shown as 157
# 7. humidity: 

import serial, sys

ser = serial.Serial('/dev/ttyUSB0', 57600)


#the original display seems to have a 2.5 variance so maybe add a 2.5 as a constant
#TMP_CONST = 2.5


while 1:

	data_raw = ser.readline().strip().split(' ')
	print(data_raw)

	temperature = (int(data_raw[5])) / 10.0  # + TMP_CONST
	humidity = int(data_raw[6]) / 10.0
	humidity = temperature / float(humidity)
	humidity_percentage = round(humidity * 100, 2)

	print('temperature: '+str(temperature)) 
	print('humidity: '+str(humidity_percentage)) 
	
	

ser.close()