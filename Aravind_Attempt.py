#checking git hahahaahah
#poda paani

import obd
import time

connection = obd.Async(baudrate=38400, fast=False) # create an asynchronous connection

# will continuously print new RPM values
def new_value1(response1):
	print(response1)

# keep track of the car's RPM
connection.watch(obd.commands.ELM_VOLTAGE, callback=new_value1)

def new_value2(response2):
	print(response2)

# keep track of the car's RPM
connection.watch(obd.commands.RPM, callback=new_value2)

def new_value3(response3):
	print(response3)

# keep track of the car's RPM
connection.watch(obd.commands.SPEED, callback=new_value3)


def new_value4(response4):
	print(response4)

# keep track of the car's RPM
connection.watch(obd.commands.RUN_TIME, callback=new_value4)

def new_value5(response5):
	print(response5)

# keep track of the car's RPM
connection.watch(obd.commands.ENGINE_LOAD, callback=new_value5)

def new_value6(response6):
	print(response6)

# keep track of the car's RPM
connection.watch(obd.commands.COOLANT_TEMP, callback=new_value6)

#print(response+'Voltage',response1+'rpm',response2+'speed',response3+'runtime',response4+'load')

connection.start()
while True:
	time.sleep(15) # do other work in the main thread
connection.stop()