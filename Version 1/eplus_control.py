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
	thermal_setpoint =float(getattr(controller,'house_'+str(i+1)+'_'+str(j+1)))
#	thermal_setpoint = float(thermal_setpoint)
	if abs(price*k)>3:
		thermal_setpoint= thermal_setpoint +np.sign(price)*3;
	else:
		thermal_setpoint= thermal_setpoint +price*k;
	
	return thermal_setpoint;
    
def thermal_setpoint_initilize(controller,houseID,NI,NJ):
	for i in range(NI):
		for j in range(NJ):
			value=72
			#np.random.uniform(74,76)
			fncs.publish(houseID[i][j]+'/cooling_setpoint', value)
			setattr(controller,houseID[i][j], value)
	return


def turn_on(i,j):
    #turn on hvac by reducing the temprature setpoints
	New_T_setpoint=60
	fncs.publish(houseID[i][j]+'/cooling_setpoint', New_T_setpoint) 
    
	return
	
def restore(i,j):
    #assign default setting, i.e. 72
	New_T_setpoint=72
	fncs.publish(houseID[i][j]+'/cooling_setpoint', New_T_setpoint) 
	return;

def turn_off(i,j):
    #turn on havac by increasing the temperature set points
	New_T_setpoint=100
	fncs.publish(houseID[i][j]+'/cooling_setpoint', New_T_setpoint) 
	return
    
def bus_shed(bus):
	for j in range(12):
		turn_off(bus-1,j)
	return
	
def bus_restore(bus):
	for j in range(12):
		restore(bus-1,j)
	return
	
def load_shed(SW):
	if SW==0:
		for bus in range(10,16):
			bus_shed(bus)
	else:
		for bus in range(10,16):
			bus_restore(bus)
	return
	
		
# requires the yaml file
class Vars:
	pass

# create house id dynamically
controller=Vars()
houseID = [[0 for i in range(12)] for j in range(15)] 
for i in range(15):
	for j in range(12):
		houseID[i][j]='house_'+str(i+1)+'_'+str(j+1) #add controller variable name dynamically
        #setattr(controller,houseID[i][j], np.random.uniform(74,78)) #randomly assign intitial thermal setpoints

import pickle
       
with warnings.catch_warnings():
	warnings.simplefilter("ignore") # TODO - pypower is using NumPy doubles for integer indices
	#warnings.filterwarnings("ignore",category=DeprecationWarning)

	if len(sys.argv) == 5:
		tmax = int(sys.argv[1])
		dt = int(sys.argv[2])
	else: 
		dt = 1
		tmax = 6*60*60
	ts = 0
	tnext = 0

	fncs.initialize()
	thermal_setpoint_initilize(controller,houseID,15,12)
     #initialize thermal setpoints for all houses
 
#	ts = -dt
#	while ts <= tmax:
#		ts += dt
	#distribution_load=[]
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
			print(value)
			if topic == 'sw_status':
				load_shed(value)
   
             
	print ('finalizing FNCS', flush=True)
	fncs.finalize()

    
    
