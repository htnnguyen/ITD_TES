#	Copyright (C) 2017 Battelle Memorial Institute
import json
import sys
import warnings
import csv
import fncs
import numpy as np
import math
import re

k=15

def house_control(i,j,price,controller):
	thermal_setpoint =float(getattr(controller,'house_'+str(i+1)+'_'+str(j+1)+'_thermostat_controller_cooling_setpoint'))
#	thermal_setpoint = float(thermal_setpoint)
	if abs(price*k)>3:
		thermal_setpoint= thermal_setpoint +np.sign(price)*3;
	else:
		thermal_setpoint= thermal_setpoint +price*k;
	
	return thermal_setpoint;
    
def thermal_setpoint_initilize(controller,houseID,NI,NJ):
	for i in range(NI):
		for j in range(NJ):
			value=np.random.uniform(74,76)
			fncs.publish('controller_'+houseID[i][j], value)
			setattr(controller,houseID[i][j], value)
	return

def logfile(name_logfile,log_value):
	old_stdout = sys.stdout
	log_file = open(name_logfile,"w")
	print(log_value)
	sys.stdout = log_file
	sys.stdout = old_stdout
	log_file.close()
	return
    
    
   

# requires the yaml file
class Vars:
	pass

# create house id dynamically
controller=Vars()
houseID = [[0 for i in range(12)] for j in range(15)] 
for i in range(15):
	for j in range(12):
		houseID[i][j]='house_'+str(i+1)+'_'+str(j+1)+'_thermostat_controller_cooling_setpoint' #add controller variable name dynamically
        #setattr(controller,houseID[i][j], np.random.uniform(74,78)) #randomly assign intitial thermal setpoints

        
with warnings.catch_warnings():
	warnings.simplefilter("ignore") # TODO - pypower is using NumPy doubles for integer indices
	#warnings.filterwarnings("ignore",category=DeprecationWarning)

	if len(sys.argv) == 5:
		tmax = int(sys.argv[1])
		dt = int(sys.argv[2])
	else: 
		dt = 300
		tmax = 2 * 24 * 3600
	ts = 0
	tnext = 0

	fncs.initialize()
	thermal_setpoint_initilize(controller,houseID,15,12)
     #initialize thermal setpoints for all houses
 
#	ts = -dt
#	while ts <= tmax:
#		ts += dt
	distribution_load=[]
	while ts <= tmax:
#		print ("looping", ts, tnext, tmax, flush=True)
		if ts >= tnext:
			tnext += dt
			if tnext > tmax:
				# print ('breaking out at',tnext,flush=True)
				break
		ts = fncs.time_request(tnext)
		events = fncs.get_events()
		for key in events:
			topic = key.decode()
			value = float(fncs.get_value(key).decode())
			if topic == 'rt_price':
				price=value
				for i in range (15):
					for j in range(12):
						New_T_setpoint=house_control(i,j,price,controller)
						fncs.publish('controller_'+houseID[i][j], New_T_setpoint) #publish new set point to hous i j in gridlab
						#setattr(controller,houseID[i][j],New_T_setpoint) # set new setpoint to controller dictionary
			if topic=='distribution_load':
				distribution_load.append(value)
				#print (distribution_load)
                      
	print ('finalizing FNCS', flush=True)
	logfile('distribution_load.txt',distribution_load)
	fncs.finalize()

    
    
