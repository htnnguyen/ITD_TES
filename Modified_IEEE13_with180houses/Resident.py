import string;
import sys;
import fncs;

time_stop = int(sys.argv[1])
time_granted = 0
time_next = 0
deltaT = 300
# requires the yaml file
fncs.initialize()

print('# time key value till', time_stop, flush=True)
alpha = 0.4
factor = 0.1

while time_granted < time_stop:
	print('Resident market time ', time_granted, flush=True)
	events = fncs.get_events()
	for key in events:
		topic = key.decode()
		print (time_granted, key, topic, fncs.get_value(key), flush=True)
		value = fncs.get_value(key).decode()
		if topic == 'MonthlyBill':
			alpha = alpha + float(value) * factor
			fncs.publish('Preference', alpha)
	# if time_granted >= time_next:
		# fncs.publish('Preference', alpha)
		# time_next += deltaT
		# if time_next > time_stop:
			# print ('breaking out at',time_next,flush=True)
			# break
	time_next = time_next + deltaT
	time_granted = fncs.time_request(time_stop) # time_next
#   print('**', time_granted)
	# events = fncs.get_events()
	# for key in events:
		# # topic = key.decode()
		# # print (time_granted, key, topic, fncs.get_value(key), flush=True)
		# # value = fncs.get_value(key).decode()
		# value = value + 0.001
		# # if topic == 'MonthlyBill':
			# # fncs.publish('Preference', alpha)

print('finalizing FNCS', flush=True)
fncs.finalize()
print('done', flush=True)
