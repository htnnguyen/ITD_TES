# import from library or functions
import fncs
import sys

def house_control(houseID,value):
	if value==(-1):
		T=85
		fncs.publish(houseID+'_cooling_setpoint', T)
		#turn off
	elif value==0:
		T=72
		fncs.publish(houseID+'_cooling_setpoint', T)
		 #restore
	elif value==1:
		T=65
		fncs.publish(houseID+'_cooling_setpoint', T)
		 #turn on
	return
   
houseID =sys.argv[1]
#fncs.initialize()
time_granted = 0 # time variable for checking the retuned time from FNCS
timeSim= 0
tf = 6 # simulation time in hours
deltaT = 60  # simulation time interval in seconds, which usually the same as controller period 
while (time_granted < tf*3600):
    # =================Simulation for each time step ============================================ 
    # Initialization when time = 0
	
	if time_granted == 0:
		fncs.initialize()
	if time_granted != 0:
		events = fncs.get_events()
		for key in events:
			topic = key.decode()
			value = float(fncs.get_value(key).decode())
			# print(value)
			if topic == houseID+'_status':
				#value1=value
				house_control(houseID,value)
	if (time_granted < (timeSim + deltaT)) :
		time_granted = fncs.time_request(timeSim + deltaT)
	else:
		timeSim = timeSim + deltaT
		time_granted = fncs.time_request(timeSim + deltaT)

fncs.finalize()        
