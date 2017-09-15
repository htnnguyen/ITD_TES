#	Copyright (C) 2017 Battelle Memorial Institute
import json
import sys
import warnings
import csv
import fncs
from ppcasefile import ppcasefile
import pypower.api as pp
import math
import re

def defaultinitilization():

    return 0

def initAuction(auctionDict):

    return 0

def check_voltage(voltage_list):
	LeastVoltage = 2401.7771
	HighestVoltage = 0.0
	#phase = voltage_list[0][1]
	for item in voltage_list:
		if item[2] < LeastVoltage:
			LeastVoltage = item[2]
	for item in voltage_list:
		if item[2] > HighestVoltage:
			HighestVoltage = item[2]
	if LeastVoltage < (0.9*2401.7771):
		Adjust_tap = 1
	elif HighestVoltage > (1.1*2401.7771):
		Adjust_tap = -1
	else:
		Adjust_tap = 0
	return Adjust_tap
	
def monitor_powerflow(power_listz,power_maximum):
	for power_list in power_listz:
		for i in range(15):
			#print(power_list)
			if ((power_list[0]==node_index[i]) and (power_list[1]==phase_index[i])):
				
				if (power_list[2]>power_maximum):
					for j in range(12):
						fncs.publish('house_'+str(i+1)+'_'+str(j+1), ThermostatMode_action)
				else:
					for j in range(12):
						fncs.publish('house_'+str(i+1)+'_'+str(j+1), ThermostatMode_default)
	return 0
def monitor_energyflow():
	return 0

    # ====================extract float from string ===============================
def get_num(self,fncs_string):
    return float(''.join(ele for ele in fncs_string if ele.isdigit() or ele == '.'))
def get_number(value):
        return float(''.join(ele for ele in value if ele.isdigit() or ele == '.'))
    
def subscribeVal(fncs_sub_value_String):
    # Assign values to buyers
    #P = []
    #Pi = []
    if "controller" in fncs_sub_value_String:
        controllerKeys = list (fncs_sub_value_String['controller'].keys())
        print('checking controllerKeys length', len(controllerKeys), flush = True)
        for i in range(len(controllerKeys)):
            #print('checking controller length', len(controller['name']), flush = True)
            for j in range(len(controller['name'])):
                #print('checking if condition: ', controller['name'][j], controllerKeys[i], flush = True)
                if controller['name'][j] == controllerKeys[i]:
                    print('air temperature: ', fncs_sub_value_String['controller'][controllerKeys[i]]['air_temperature'], flush=True)
                    controller['air_temperature'][j] = fncs_sub_value_String['controller'][controllerKeys[i]]['air_temperature']
                    Pi.append(controller['theta'][j] * fncs_sub_value_String['controller'][controllerKeys[i]]['air_temperature'])
                    P.append(controller['P'][j])
                    #print('P value: ', controller['P'][j], flush=True)
                    #print('Pi value: ', controller['theta'][j] * fncs_sub_value_String['controller'][controllerKeys[i]]['air_temperature'], flush=True)
                    #print('Pi vector: ', Pi)
                #print('Pi val: ', Pi, flush= True)
        #print('P val: ', P, flush=True)
    return 0


def calClearPrice(error, Pi):
    sum = 0
    #[Pi_sorted, indexlist] = sort_prices(Pi)
    indexlist = []
    CP = 1.0
    sortedlist = sorted(enumerate(Pi), key = lambda x: x[1])
    print('printing sorted list:', sortedlist, flush = True)
    for i in sortedlist:
        indexlist.append(i[0])
        Pi_sorted.append(i[1])
    print('printing index list:', indexlist, flush = True)
    print('printing Pi_sorted list:', Pi_sorted, flush = True)
    
    for i in range(len(indexlist)):
        P_sorted.append(P[indexlist[i]])
    print('printing P_sorted list:', P_sorted, flush = True)

    for i in range(len(P_sorted)):
        sum = sum + P_sorted[i]
        print('printing sum:', sum, error, flush = True)
        if sum >= error:
            print('printing sum again:', sum, error, Pi_sorted[i], flush = True)
            CP = Pi_sorted[i]
            return Pi_sorted[i]
    return CP
    
def sort_prices(Pi):
	valueslist = []
	indexlist =[]
	sortedlist = sorted(enumerate(Pi), key = lambda x: x[1])
	for i in sortedlist:
		indexlist.append(i[0])
		valueslist.append(i[1])
	print('Values list: ', valueslist, flush=True)
	return [valueslist, indexlist]

def publish_Price(value):
	#print('checking before updation',fncs_publish['auction'][market['name']]['price_cap']['propertyValue'], flush = True)
	fncs_publish['auction'][market['name']]['market_id']['propertyValue'] = 1
	fncs_publish['auction'][market['name']]['std_dev']['propertyValue'] = 0.01
	fncs_publish['auction'][market['name']]['average_price']['propertyValue'] = 0.02078
	fncs_publish['auction'][market['name']]['clear_price'] = value
	fncs_publish['auction'][market['name']]['price_cap']['propertyValue'] = 3.78
	fncs_publish['auction'][market['name']]['period']['propertyValue'] = 300
	fncs_publish['auction'][market['name']]['initial_price']['propertyValue'] = 0.02078
	
	fncs_publishString = json.dumps(fncs_publish)
	fncs.agentPublish(fncs_publishString)
	fncs.publish('clear_price', value)
	# for i in range(15):
		# for j in range(12):
			# print('publishing WP: ', value,flush = True)
			# fncs.publish('clear_price'+'_'+'house_'+str(i+1)+'_'+str(j+1), value)
	return 0
	
tapA = 0
tapB = 0
tapC = 0
voltage_listA=[]
voltage_listB=[]
voltage_listC=[]

power_listA=[]
power_listB=[]
power_listC=[]
energy_listA = []
energy_listQ = []
WP = [0.0 for i in range(24)]
WRP = [0.0 for i in range(24*60)]
delTWRP = 60
delTAuction = 1
	
with warnings.catch_warnings():
	warnings.simplefilter("ignore") # TODO - pypower is using NumPy doubles for integer indices
	#warnings.filterwarnings("ignore",category=DeprecationWarning)
	stats = {'stat_mode': [], 'interval': [], 'stat_type': [], 'value': [], 'statistic_count': 0}
	market = {'name': 'none',' period': -1, 'latency': 0, 'market_id': 1, 'network': 'none', 'linkref': 'none', 'pricecap': 0.0, 
					'special_mode': 'MD_NONE', 'statistic_mode': 1, 'fixed_price': 50.0, 'fixed_quantity': 0.0,
					'init_price': 0.0, 'init_stdev': 0.0, 'future_mean_price': 0.0, 'use_future_mean_price': 0, 
					'capacity_reference_object': {'name': 'none', 'capacity_reference_property': 0.0, 'capacity_reference_bid_price': 0.0, 
                                                 'max_capacity_reference_bid_quantity': 0.0, 'capacity_reference_bid_quantity': 0.0},
					'current_frame': {'start_time': 0.0, 'end_time': 0.0, 'clearing_price':0.0, 'clearing_quantity': 0.0, 'clearing_type': 'CT_NULL', 
                                      'marginal_quantity': 0.0, 'total_marginal_quantity': 0.0, 'marginal_frac': 0.0, 'seller_total_quantity': 0.0, 
                                      'buyer_total_quantity': 0.0, 'seller_min_price': 0.0, 'buyer_total_unrep': 0.0, 'cap_ref_unrep': 0.0, 
                                      'statistics': []}, 
					'past_frame': {'start_time': 0.0, 'end_time': 0.0, 'clearing_price':0.0, 'clearing_quantity': 0.0, 'clearing_type': 'CT_NULL', 
                                      'marginal_quantity': 0.0, 'total_marginal_quantity': 0.0, 'marginal_frac': 0.0, 'seller_total_quantity': 0.0, 
                                      'buyer_total_quantity': 0.0, 'seller_min_price': 0.0, 'buyer_total_unrep': 0.0, 'cap_ref_unrep': 0.0, 
                                      'statistics': []}, 
					'cleared_frame': {'start_time': 0.0, 'end_time': 0.0, 'clearing_price':0.0, 'clearing_quantity': 0.0, 'clearing_type': 'CT_NULL', 
                                      'marginal_quantity': 0.0, 'total_marginal_quantity': 0.0, 'marginal_frac': 0.0, 'seller_total_quantity': 0.0, 
                                      'buyer_total_quantity': 0.0, 'seller_min_price': 0.0, 'buyer_total_unrep': 0.0, 'cap_ref_unrep': 0.0, 
                                      'statistics': []}, 
					'margin_mode': 'AM_NONE', 'ignore_pricecap': 0,'ignore_failedmarket': 0, 'warmup': 1,
					'total_samples': 0,'clearat': 0,  'clearing_scalar': 0.5, 'longest_statistic': 0.0}  
        
	market_output = {'std': -1, 'mean': -1, 'clear_price': -1, 'market_id': 'none', 'pricecap': 0.0} # Initialize market output with default values
	buyer = {'name': [], 'price': [], 'quantity': [], 'state': [], 'bid_id': []}
	seller = {'name': [], 'price': [], 'quantity': [], 'state': [], 'bid_id': []} 
	nextClear = {'from':0, 'quantity':0, 'price':0}
	offers = {'name': [], 'price': [], 'quantity': []}
	controller = {'name': [], 'price': [], 'quantity': [], 'state': [], 'Tbliss': [], 'd': [], 'theta': [], 'P': [], 'houseType': [], 'air_temperature': []}
	housedata = {'name': 'none', 'air_temperature': 78, 'state': 'ON', 'Tbliss': 75, 'd': 10, 'theta': 1.0, 'P': 2.1, 'houseType': 'none', 'price': 0.0, 'quantity': 0.0}
	housedataArray = []
	PControlSignal = 10

	if len(sys.argv) == 6:
		filename = sys.argv[1]
		rootname = sys.argv[2]
		StartTime = sys.argv[3]
		tmax = int(sys.argv[4])
		dt = int(sys.argv[5])
	elif len(sys.argv) == 1:
		rootname = 'ppcase'
		StartTime = "2013-07-01 00:00:00"
		dt = 3600
		tmax = 2 * 24 * 3600
	else:
		print ('usage: python fncsPYPOWER.py [rootname StartTime tmax dt]')
		sys.exit()
	lp = open(filename).read()
	auctionDict = json.loads(lp)
	agentRegistration = auctionDict['registration']
	agentInitialVal = auctionDict['initial_values']
	print('Market Name', agentRegistration['agentName'], market['name'], flush = True)
	market['name'] = agentRegistration['agentName']
	print('Market Name', agentRegistration['agentName'], market['name'], flush = True)
	# Read and assign initial values from agentInitialVal
	# Market information
	market['special_mode'] = agentInitialVal['market_information']['special_mode']
	market['market_id'] = agentInitialVal['market_information']['market_id']
	market['use_future_mean_price'] = agentInitialVal['market_information']['use_future_mean_price']
	market['pricecap'] = agentInitialVal['market_information']['pricecap']
	market['clearing_scalar'] = agentInitialVal['market_information']['clearing_scalar']
	market['period'] = agentInitialVal['market_information']['period']
	market['latency'] = agentInitialVal['market_information']['latency']
	market['init_price'] = agentInitialVal['market_information']['init_price']
	market['init_stdev'] = agentInitialVal['market_information']['init_stdev']
	market['ignore_pricecap'] = agentInitialVal['market_information']['ignore_pricecap']
	market['ignore_failedmarket'] = agentInitialVal['market_information']['ignore_failedmarket']
	market['statistic_mode'] = agentInitialVal['market_information']['statistic_mode']
	market['capacity_reference_object']['name'] = agentInitialVal['market_information']['capacity_reference_object']
	market['capacity_reference_object']['max_capacity_reference_bid_quantity'] = agentInitialVal['market_information']['max_capacity_reference_bid_quantity']
    
    # Stats information
	stats['stat_mode'] = agentInitialVal['statistics_information']['stat_mode']
	stats['interval'] = agentInitialVal['statistics_information']['interval']
	stats['stat_type'] = agentInitialVal['statistics_information']['stat_type']
	stats['value'] = agentInitialVal['statistics_information']['value']
    
    # Controller information
	controller['name'] = agentInitialVal['controller_information']['name']
	controller['price'] = agentInitialVal['controller_information']['price']
	controller['quantity'] = agentInitialVal['controller_information']['quantity']
	controller['state'] = agentInitialVal['controller_information']['state']
	print('check Tbliss:', agentInitialVal['controller_information']['Tbliss'], flush = True)
	controller['Tbliss'] = agentInitialVal['controller_information']['Tbliss']
	controller['d'] = agentInitialVal['controller_information']['d']
	controller['theta'] = agentInitialVal['controller_information']['theta']
	controller['P'] = agentInitialVal['controller_information']['P']
	controller['houseType'] = agentInitialVal['controller_information']['houseType']
	controller['air_temperature'] = agentInitialVal['controller_information']['air_temperature']

	RealPowerkWh = {}
	for i in range(len(controller['name'])):
		S = controller['name'][i].split('_thermostat_controller')
		RealPowerkWh[S[0]] = {'real_power_kWh' : 0.0, 'energybillmin': 0.0, 'Prev_real_power_kWh' : 0.0}
	print('Realpowerkwhhouse: ', RealPowerkWh, flush=True)
	for i in range(0,len(agentInitialVal)):
		s = agentInitialVal['controller_information']['name'][i]
		print('s', s, flush = True)
		housedata['name'] = s
		housedata['price'] = agentInitialVal['controller_information']['price'][i]
		housedata['quantity'] = agentInitialVal['controller_information']['quantity'][i]
		housedata['state'] = agentInitialVal['controller_information']['state'][i]
		housedata['Tbliss'] = agentInitialVal['controller_information']['Tbliss'][i]
		housedata['d'] = agentInitialVal['controller_information']['d'][i]
		housedata['theta'] = agentInitialVal['controller_information']['theta'][i]
		housedata['P'] = agentInitialVal['controller_information']['P'][i]
		housedata['houseType'] = agentInitialVal['controller_information']['houseType'][i]
		housedata['air_temperature'] = agentInitialVal['controller_information']['air_temperature'][i]
		housedataArray.append(housedata)
        
    # Generate agent publication dictionary
	fncs_publish = {
		'auction': {
			market['name']: {
				'market_id': {'propertyType': 'integer', 'propertyUnit': 'none', 'propertyValue': 0},
				'std_dev': {'propertyType': 'integer', 'propertyUnit': 'none', 'propertyValue': 0.0},
				'average_price': {'propertyType': 'double', 'propertyUnit': 'none', 'propertyValue': 0.0},
				'clear_price': {'propertyType': 'double', 'propertyUnit': 'none', 'propertyValue': 0.0},
				'price_cap': {'propertyType': 'integer', 'propertyUnit': 'none', 'propertyValue': 0.0},
				'period': {'propertyType': 'double', 'propertyUnit': 'none', 'propertyValue': -1.0},
				'initial_price':{'propertyType': 'double', 'propertyUnit': 'none', 'propertyValue': 0.0}
				}
			}
		}
	fncs_publish['auction'][market['name']]['clear_price'] = 0.002
	fncs.publish('clear_price', 0.002)
	ts = 0
	tnext = 0
	tnextBill = 300
	dtBill = 300 #2592000
	MonthlyBill = 20
	fncs.initialize()
	iter = 1

#	ts = -dt
#	while ts <= tmax:
#		ts += dt
	p = 0.0167
	a = 0.004
	c = -1
	while ts <= tmax:
		print ("looping", ts, tnext, tmax, flush=True)
		# if ts >= tnext:
			# c = c + 1
			# fncs.publish('LMP_B7', 0.0157)			
			# tnext += dt
			# if tnext > tmax:
				# print ('breaking out at',tnext,flush=True)
				# break
		if ts >= tnextBill:
			fncs.publish('MonthlyBill', MonthlyBill)
			tnextBill += dtBill
			if tnextBill > tmax:
				print ('breaking out at',tnextBill,flush=True)
				break
		tnext += delTAuction
		ts = fncs.time_request(tnext)
		fncs_sub_value_unicode = (fncs.agentGetEvents()).decode()
		if fncs_sub_value_unicode != '':
			#Global variables
			P = []
			Pi = []
			P_sorted = []
			Pi_sorted = []
			fncs_sub_value_String = json.loads(fncs_sub_value_unicode)
			subscribeVal(fncs_sub_value_String)
			#printing data to test sorting:
			#print('Pi values: ', Pi, flush=True)
			#print('P values: ', P, flush=True)
			#print('Clear Price: ', calClearPrice(100,Pi), flush = True)
			#print('Pi_sorted values: ', Pi_sorted, flush=True)
		events = fncs.get_events()
		for key in events:
			title = key.decode()
			value = fncs.get_value(key).decode()
			if title.startswith('RealPowerkWh'):
				S = title.split('#')
				RealPowerkWh[S[1]]['real_power_kWh']= get_number(value)
				print ('RealPowerkWh: ',RealPowerkWh[S[1]]['real_power_kWh'], flush = True)
				if ts % delTWRP == 0:
					for i in range(len(RealPowerkWh)):
						if ts!=0:
							# print ('checking..', RealPowerkWh[S[1]]['energybillmin'], flush = True)
							# print ('checking..', RealPowerkWh[S[1]]['Prev_real_power_kWh'], flush = True)
							# print ('checking..', RealPowerkWh[S[1]]['real_power_kWh'], flush = True)
							# print ('checking..', iter, flush = True)
							# print ('checking..', WRP[iter-1], flush = True)
							RealPowerkWh[S[1]]['energybillmin'] = RealPowerkWh[S[1]]['energybillmin'] + WRP[iter-1] * (RealPowerkWh[S[1]]['real_power_kWh'] - RealPowerkWh[S[1]]['Prev_real_power_kWh'])
							iter += 1
							if iter > 24*60:
								iter = 1
							RealPowerkWh[S[1]]['Prev_real_power_kWh'] = RealPowerkWh[S[1]]['real_power_kWh']
					print('printing WRP', WRP[iter], flush = True) 
					publish_Price(WRP[iter])
				#fncs.publish('ResetRealPower', 0)
			if title.startswith('tap'):
				if title == 'tapA':
					tapA = int(value)
				elif title == 'tapB':
					tapB = int(value)
				elif title == 'tapC':
					tapC = int(value)	
				#print('tapABC', tapA, tapB, tapC, flush = True)
			# price
			if title.startswith('Error'):
				ErrorSignal = float(value)
				Pi_Cleared = calClearPrice(ErrorSignal,Pi)
				print('Pi_sorted values: ', Pi_sorted, flush=True)
				print('Clear Price: ', Pi_Cleared, flush = True)
				#publish_Price(Pi_Cleared)
			if title.startswith('WholesalePriceDAM'):
				WP = value
				WRP = [i for i in WP for j in range(60)]
				#publish_Price(float(value))
				#print('checking outside method',fncs_publish['auction'][market['name']]['price_cap']['propertyValue'], flush = True)
			# if title.startswith('WP'):
				# print('wp:price',value,flush = True)
				# fncs.publish('WP', value)
				#publish_WP(value)
			# voltage
			#fncs.publish('LMP_DSO', 0.0164)
			if title.startswith('voltage'):
				if value.endswith('V'):
					valuesplit = value.split(' ')
					valuedecoded = valuesplit[0]
					valuecomplex = complex(valuedecoded)
					absvalue = abs(valuecomplex)
					#print('Split: ', valuecomplex, absvalue, flush = True)			
				if title[-2:]=='AN':
					if len(voltage_listA)>0:
						for item in voltage_listA:
							if item[0]==title[-5:-2]:
								item[2] = absvalue
							else:
								voltage_listA.append([title[-5:-2], title[-2:], absvalue])
					else:
						voltage_listA.append([title[-5:-2], title[-2:], absvalue])
	#				node_listA.append()
				if title[-2:]=='BN':
					if len(voltage_listB)>0:
						for item in voltage_listB:
							if item[0]==title[-5:-2]:
								item[2] = absvalue
							else:
								voltage_listB.append([title[-5:-2], title[-2:], absvalue])
					else:
						voltage_listB.append([title[-5:-2], title[-2:], absvalue])						
				if title[-2:]=='CN':
					if len(voltage_listC)>0:
						for item in voltage_listC:
							if item[0]==title[-5:-2]:
								item[2] = absvalue
							else:
								voltage_listC.append([title[-5:-2], title[-2:], absvalue])
					else:
						voltage_listC.append([title[-5:-2], title[-2:], absvalue])
			
		#print('tapABC', tapA, tapB, tapC, flush = True)
		Adjust_tap_A = check_voltage(voltage_listA)
		UpdateTapA = tapA + Adjust_tap_A	
		#print('Adjust TapA', Adjust_tap_A, 'Updated TapA', UpdateTapA, flush = True)
		fncs.publish('reg_statusTapA', UpdateTapA)
		Adjust_tap_B = check_voltage(voltage_listB)
		UpdateTapB = tapB + Adjust_tap_B	
		#print('Adjust TapB', Adjust_tap_B, 'Updated TapB', UpdateTapB, flush = True)
		fncs.publish('reg_statusTapB', UpdateTapB)	
		Adjust_tap_C = check_voltage(voltage_listC)
		UpdateTapC = tapC + Adjust_tap_C
		#print('Adjust TapC', Adjust_tap_C, 'Updated TapC', UpdateTapC, flush = True)
		fncs.publish('reg_statusTapC', UpdateTapC)
		# for key in events:
			# substation = key.decode()
			# GLDload = parse_mva (fncs.get_value(key).decode())
# #			print ('  **', ts, substation, GLDload)
			# for row in fncsBus:
				# if substation == row[1]:
# #					print('    assigning',substation,GLDload)
					# row[3] = GLDload[0]

#	summarize_opf(res)
	# print ('writing metrics', flush=True)
	# print (json.dumps(bus_metrics), file=bus_mp, flush=True)
	# print (json.dumps(gen_metrics), file=gen_mp, flush=True)
	# print (json.dumps(sys_metrics), file=sys_mp, flush=True)
	# print ('closing files', flush=True)
	# bus_mp.close()
	# gen_mp.close()
	# sys_mp.close()
	# op.close()
	print ('finalizing FNCS', flush=True)
	fncs.finalize()

