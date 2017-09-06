#	Copyright (C) 2017 Battelle Memorial Institute
#import json
import sys
import fncs

			
#writting to json file
def turn_on(i,j):
	#turn on hvac by reducing the temprature setpoints
	fncs.publish('house_'+str(i)+'_'+str(j)+'_status', 1)
	return
	
def restore(i,j):
	fncs.publish('house_'+str(i)+'_'+str(j)+'_status', 0)
	return

def turn_off(i,j):
	fncs.publish('house_'+str(i)+'_'+str(j)+'_status', -1)
	return
 
def bus_shed(bus):
	for j in range(12):
		turn_off(bus,j+1)
	return
	
def bus_restore(bus):
	for j in range(12):
		restore(bus,j+1)
	return
	
def bus_on(bus):
	for j in range(12):
		turn_on(bus,j+1)
	return
	
def load_shed(SW):
	#Load shed example, we shut down node 10-15
	if SW==1:
		for bus in range(10,16):
			bus_restore(bus)
	elif SW==0:
		for bus in range(10,16):
			bus_shed(bus)
	else:
		for bus in range(10,16):
			bus_on(bus)
	return
	
# fncs.initialize()
houseID = [[0 for j in range(12)] for i in range(15)] 

for i in range(15):
	for j in range(12):
		houseID[i][j]='house_'+str(i+1)+'_'+str(j+1)#add controller variable name dynamically

time_granted = 0 # time variable for checking the retuned time from FNCS
timeSim= 0

time_granted=0
time_granted = 0 # time variable for checking the retuned time from FNCS
timeSim= 0
#fncs.initialize()
value =0
tf = 48 # simulation time in hours
deltaT = 1  # simulation time interval in seconds, which usually the same as controller period 
while (time_granted < tf*3600):
    # =================Simulation for each time step ============================================ 
    # Initialization when time = 0
	
	if time_granted == 0:
		fncs.initialize()
	if time_granted != 0:
		events = fncs.get_events()
		for key in events:
			topic = key.decode()
			value1 = float(fncs.get_value(key).decode())
			if topic == 'sw_status':
				value=value1
				load_shed(value)
	if (time_granted < (timeSim + deltaT)) :
		time_granted = fncs.time_request(timeSim + deltaT)
	else:
		timeSim = timeSim + deltaT
		time_granted = fncs.time_request(timeSim + deltaT)

fncs.finalize()

