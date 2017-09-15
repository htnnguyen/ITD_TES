import sys
import numpy as np
k=['CS','AS','BS','CS','BS','CS','BS','CS','AS','AS','BS','CS','AS','BS','CS']
with open('IEEE13VariableDatatest.glm', 'a') as sys.stdout:
	for i in range(1,15):
		for j in range(1,12):
			print('object house {')
			print('name house_'+str(i)+'_'+str(j)+';')
			print('parent trip_meter'+str(i)+'_'+str(j)+';')
			print('thermostat_control NONE;')
			print('system_mode COOL;')
			print('hvac_power_factor 0.97;')
			print('heating_system_type ', end='')
			x=np.random.random_sample()
			if x<0.7112:
				print('GAS;')
			elif x>=0.7112 and x<0.8722:
				print('HEAT_PUMP;')
			else:
				print('RESISTANCE;')
				
			print('cooling_system_type ', end='')
			if x<0.947:
				if x <= 1:
					print('ELECTRIC;')
				else:
					print('NONE;')

			print('cooling_COP 3.90;')
			print('floor_area random.normal(1700,400);')
			#normrnd(1700,400)) equivalent in python
			#s1 ='floor_area '+ '' + str(np.random.normal(1700, 400)
			#print('%s;',s1)
			#print('')
			#print(strcat({'cooling_setpoint '},{''},{num2str(unifrnd(74,78))}))
			#print('')
			#print('thermostat_deadband 1;')
			print('ceiling_height 10;')
			print('window_wall_ratio 0.1;')
			print('Rwall random.uniform(13,15);')
			print('Rwall '+''+str(np.random.uniform(13,15))+';')#unifrnd(13,15)))
			print('Rwindows random.uniform(0.8,1);')
			print('Rwindow '+''+str(np.random.uniform(0.8,1)))#unifrnd(0.8,1)))
			print('Rroof random.uniform(38,60);')
			print('object ZIPload {')
			print('schedule_skew random.uniform(-1000,1000);')
			print('base_power LIGHTS*',end='')
			#y1=0.087*randi([70,120],1)/100
			y1 = 0.087*np.random.randint(70,120)/100
			print(str(y1) + ';')
			print('power_fraction -0.04000;')
			print('impedance_fraction 0.540000;')
			print('current_fraction 0.50000;')
			print('power_pf -1;')
			print('current_pf 1;')
			print('impedance_pf 1;')
			print('heat_fraction 0.91;')
			print('};')
			print('object waterheater {')
			print('schedule_skew random.uniform(-1000,1000);')
			print('heat_mode ', end='')
			#x1 = rand;
			x1=np.random.random_sample()
			if x1<0.43:
				print('ELECTRIC;')
			else:
				print('GASHEAT;')

			print('tank_volume random.uniform(20,80);')
			print('heating_element_capacity random.uniform(4,5);')
			print('tank_setpoint random.uniform(110,120);')
			print('temperature 135;')
			print('thermostat_deadband random.uniform(5,10);')
			print('location INSIDE;')
			print('tank_UA 3.7;')
			print('demand water*1;')
			print('};')
			x2=np.random.random_sample()
			if x2<0.9536:
				print('object ZIPload {')
				print('schedule_skew random.uniform(-1000,1000);')
				print('base_power CLOTHESWASHER*0.4354;')
				print('power_fraction 1.000000;')
				print('impedance_fraction 0.000000;')
				print('current_fraction 0.000000;')
				print('power_pf 0.970;')
				print('current_pf 0.970;')
				print('impedance_pf 0.970;')
				print('heat_fraction 0.70;')
				print('};')
			x3=np.random.random_sample()
			if x3<0.997:
				print('object ZIPload {')
				print('schedule_skew random.uniform(-1000,1000);')
				print('base_power REFRIGERATOR*')
				#y2=0.12*randi([70,120],1)/100;
				y2=0.12*np.random.randint(70,120)/100
				print(str(y2)+';')
				print('power_fraction 4.450000;')
				print('impedance_fraction 5.030000;')
				print('current_fraction -8.480000;')
				print('power_pf 0.640;')
				print('current_pf 0.560;')
				print('impedance_pf 0.550;')
				print('heat_fraction 0.86;')
				print('};')
			
			x4=np.random.random_sample()
			
			if x4<0.9503:
				print('object ZIPload {')
				print('schedule_skew random.uniform(-1000,1000);')
				print('base_power DRYER*1.0019;')
				print('power_fraction 0.100000;')
				print('impedance_fraction 0.800000;')
				print('current_fraction 0.100000;')
				print('power_pf 0.900;')
				print('current_pf 0.900;')
				print('impedance_pf 1.000;')
				print('heat_fraction 0.77;')
				print('};')
			
			x5=np.random.random_sample()
			
			if x5<0.95:
				print('object ZIPload {')
				print('schedule_skew random.uniform(-1000,1000);')
				print('base_power FREEZER*0.9110;')
				print('power_fraction 1.000000;')
				print('impedance_fraction 0.000000;')
				print('current_fraction 0.000000;')
				print('power_pf 0.970;')
				print('current_pf 0.970;')
				print('impedance_pf 0.970;')
				print('heat_fraction 0.80;')
				print('};')

			x6=np.random.random_sample()
			if x6<0.997:
				print('object ZIPload {')
				print('schedule_skew random.uniform(-1000,1000);')
				print('base_power RANGE*1.0590;')
				print('power_fraction 0.000000;')
				print('impedance_fraction 1.000000;')
				print('current_fraction 0.000000;')
				print('power_pf 0.000;')
				print('current_pf 0.000;')
				print('impedance_pf 1.000;')
				print('heat_fraction 0.86;')
				print('};')

			print('object ZIPload {')
			print('schedule_skew random.uniform(-1000,1000);')
			print('base_power MICROWAVE*')
			#y3=1.36553*randi([70,120],1)/100;
			y3 = 1.36553*np.random.randint(70,120)/100
			print(str(y3)+';')
			print('power_fraction 0.110000;')
			print('impedance_fraction 1.160000;')
			print('current_fraction -0.270000;')
			print('power_pf 0.02540;')
			print('current_pf -0.12560;')
			print('impedance_pf -0.05220;')
			print('heat_fraction 0.94;')
			print('};')
			print('}')

	print( '#include "outputs_te.glm";')