#	Copyright (C) 2017 Battelle Memorial Institute
#import json
import sys
import fncs
import numpy as np
import json
import matplotlib.pyplot as plt

def market_clearing(power_error,total_hvac,list_pistar,list_power_level):
	#market clearing process based on PowerMathcher
	pmax=0.1
	#sort the power and price
	power=[]
	price=[]
	for i in range(15):
		for j in range(12):
			power.append(float(list_power_level[i][j])); #read the power and price in one dimensional lists
			price.append(float(list_pistar[i][j]));
	#power = [power for _, power in sorted(zip(price,power))] #sorted power based on price (increasing order)
	price = sorted(price) #sorted price (increasing order)
	sort_index=sorted(range(len(price)), key=lambda k: price[k])
	#create the aggregated power curve
	power = [ power[i] for i in sort_index]
	acc_power=power;
	for i in range(len(price)):
		acc_power[i]=sum(power[i:])
	new_hvac_load=total_hvac + power_error
	index = min(range(len(acc_power)), key=lambda i: abs(acc_power[i]-new_hvac_load))
	clear_price = price[index]
	
	if clear_price > pmax:
		clear_price =pmax
	if clear_price < 0:
		clear_price =0
	print('total hvac: ',total_hvac)
	print('accumulated power (in the power demand curve): ', acc_power[index])
	print('new hvac: ', new_hvac_load)
	#output=[clear_price,total_hvac,acc_power[index],new_hvac_load]
	return clear_price


def hvac_energy_consumtion(list_rt_power,list_pistar):
	total = 0
	for i in range(15):
		for j in range(12):
			total=total +list_rt_power[i][j]
	return total


def hvac_sort_houses(house_pistar):
	return (sorted(house_pistar.items(), key = lambda x: x[1]))
# fncs.initialize()
houseID = [[0 for j in range(12)] for i in range(15)] 
list_pistar = [[0 for j in range(12)] for i in range(15)] 
list_rt_power= [[0 for j in range(12)] for i in range(15)] 
list_power_level = [[0 for j in range(12)] for i in range(15)] 

for i in range(15):
	for j in range(12):
		houseID[i][j]='house_'+str(i+1)+'_'+str(j+1)#add controller variable name dynamically


time_granted = 0 # time variable for checking the retuned time from FNCS
timeSim= 0
#fncs.initialize()

value =0
tf = 24 # simulation time in hours
deltaT = 30  # simulation time interval in seconds(minutes), which usually the same as controller period 

hour_factor = 3600/(deltaT) #1 hour = ? time intervals .e.g one hour = 120 (30 sec) intervals
minute_factor =60/(deltaT)
#the market price is annouced every 5 mins

power_error=0
pmax=0.1
flag=0
clprice=[]
dload=[]
bline=[]

sub_time=0
while (time_granted < tf*3600):
	# =================Simulation for each time step ============================================ 
	# Initialization when time = 0
	
	if time_granted == 0:
		fncs.initialize()
		sub_time=0
	if time_granted != 0:
		events = fncs.get_events()
		for key in events:
			topic = key.decode()
			for i in range(15):
				for j in range(12):
					if topic == houseID[i][j]+ '_bidding_curves_pistar':
						value = float(fncs.get_value(key).decode())
						list_pistar[i][j]=value
					if topic == houseID[i][j]+ '_power_level':
						value = float(fncs.get_value(key).decode())
						list_power_level[i][j]=value
					if topic == houseID[i][j]+ '_rt_power':
						value = float(fncs.get_value(key).decode())
						list_rt_power[i][j]=value
			if topic == 'base_line':
				value = float(fncs.get_value(key).decode())
				base_line= value

			if topic == 'distribution_load':
				value = fncs.get_value(key).decode()
				value = value.replace('VA', '')
				distribution_load=np.real(complex(value))

		#print('check total hvac: ', total_hvac)
		#clear_price=market_clearing(power_error,total_hvac,list_pistar,list_power_level)

	if (time_granted < (timeSim + deltaT)) :
		time_granted = fncs.time_request(timeSim + deltaT)
	else:
		timeSim = timeSim + deltaT
		power_error= base_line - distribution_load
		sub_time= sub_time+1
		total_hvac= hvac_energy_consumtion(list_rt_power,list_pistar)
		bline.append(base_line)
		hour = int(len(bline)/hour_factor)
		minute = (len(bline)- hour*hour_factor)/(minute_factor)
		print('hour: ', hour, ' minutes: ',minute  )
		print('base_line: ', base_line)
		print('distribution load: ', distribution_load)
		print('base_line - distribution_load:',power_error)
		dload.append(distribution_load)
		#clear price
		clear_price=market_clearing(power_error,total_hvac,list_pistar,list_power_level)
		print('************************************************')
		print('************************************************')
		if sub_time >=10:
			sub_time=0
			fncs.publish('clear_price', clear_price)
			print('clear_price for next 5 mins:', clear_price)
			#clprice.append(clear_price)
			clprice.extend([clear_price for i in range(10)])
		time_granted = fncs.time_request(timeSim + deltaT)
		
		#announce price every 5 mins
		#sub_time=0
		#print('*******DLOAD**************')
		#print(dload)
		#print('*******BLINE**************')
		#print(bline)



print('*******DLOAD**************')
print(dload)
print('*******BLINE**************')
print(bline)
#json.dumps(clprice) 

#prepare stick
ind =[ i for i in range(0,len(dload)+int(hour_factor),int(hour_factor))]
str_stick =[ str(int((i+0.00001)/hour_factor)) for i in ind]
#Plotting dload and bline
fig = plt.figure(1)
plt.subplot(211)
t = range(len(dload))
p1=plt.plot(t, dload, 'b', )
p2=plt.plot(t, bline, 'r', )
plt.xlabel("Time (h)")
plt.ylabel("Power (W)")
plt.xticks(ind,str_stick)


#now you can plot the price  clprice ?????????????????????????????????????????????????????????
plt.subplot(212)
t2 = range(len(clprice))
p3=plt.plot(t2, clprice,)
plt.xlabel("Time (h)")
plt.ylabel("Price")
plt.xticks(ind,str_stick)
plt.legend((p1[0], p2[0], p3[0]), ('Distribution Load (Price controlled scheme)', 'Base Line','Cleared Price'))
plt.show()

print('***********************************Price**************************************************')
print(clprice)

fncs.finalize()

