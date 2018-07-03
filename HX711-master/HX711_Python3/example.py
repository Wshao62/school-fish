#!/usr/bin/env python3
from hx711 import HX711		# import the class HX711
import RPi.GPIO as GPIO		# import GPIO

try:
	# Create an object hx which represents your real hx711 chip
	# Required input parameters are only 'dout_pin' and 'pd_sck_pin'
	# If you do not pass any argument 'gain_channel_A' then the default value is 128
	# If you do not pass any argument 'set_channel' then the default value is 'A'
	# you can set a gain for channel A even though you want to currently select channel B
	hx = HX711(dout_pin=2, pd_sck_pin=3, gain_channel_A=128, select_channel='A')
	
	result = hx.reset()		# Before we start, reset the hx711 ( not necessary)
	if result:			# you can check if the reset was successful
		print('Ready to use')
	else:
		print('not ready')
	
	hx.set_gain_A(gain=64)		# You can change the gain for channel A  at any time.
	hx.select_channel(channel='A')	# Select desired channel. Either 'A' or 'B' at any time.
	
	# Read data several, or only one, time and return mean value
	# it just returns exactly the number which hx711 sends
	# argument times is not required default value is 1
	data = hx.get_raw_data_mean(times=1)
	
	if data != False:	# always check if you get correct value or only False
		print('Raw data: ' + str(data))
	else:
		print('invalid data')
	
	print("初始化_歸零準位")
	# measure tare and save the value as offset for current channel
	# and gain selected. That means channel A and gain 64
	result = hx.zero(times=10)
	
	# Read data several, or only one, time and return mean value.
	# It subtracts offset value for particular channel from the mean value.
	# This value is still just a number from HX711 without any conversion
	# to units such as grams or kg.
	while True:
		data = hx.get_data_mean(times=10)
		print(data/1000)

	
except (KeyboardInterrupt, SystemExit):
	print('Bye :)')
	
finally:
	GPIO.cleanup()

