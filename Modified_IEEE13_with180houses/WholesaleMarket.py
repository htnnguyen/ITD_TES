import string;
import sys;
import fncs;
import random;

time_stop = int(sys.argv[1])
time_granted = 0
time_next = 0
time_grantedDAM = 0
time_nextDAM = 0
delT = 60
delTDAM = 86400
# requires the yaml file
fncs.initialize()

print('# time key value till', time_stop, flush=True)

def publish_WholesalePrice(value):
	fncs.publish('WholesalePrice', value)
	return 0

a = 0.01
b = 0.025
WP = []
for i in range(24):
    WP.append(random.uniform(a,b))
print('WholesalePriceDAM', WP, flush = True)
error = [40, 50, 60, 70, 80, 90, 100, 110, 120, 90, 80, 60, 30, 40, 40, 60, 70, 80, 90, 100, 110, 120, 90, 80, 60, 30, 40, 40, 50, 50]
#error = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0

while time_granted < time_stop:
	print('wholesale market time ', time_granted, flush=True)
	if time_grantedDAM >= time_nextDAM:
		fncs.publish('WholesalePriceDAM', WP)
		print('WholesalePriceDAM', WP, flush = True)
	if time_granted >= time_next:
		fncs.publish('Error', error[i])
		i += 1
		if i >= len(error):
			i = 0
		time_next += delT
		time_nextDAM += delTDAM
		if time_next > time_stop:
			print ('breaking out at',time_next,flush=True)
			break
	time_granted = fncs.time_request(time_next) # time_next
	time_grantedDAM = fncs.time_request(time_next) # time_next
	# events = fncs.get_events()
	# for key in events:
		# topic = key.decode()
		# # print (time_granted, key, topic, fncs.get_value(key), flush=True)
		# value = fncs.get_value(key).decode()
		# if topic == 'WholesalePrice':
			# fncs.publish('WholesalePrice', value)

print('finalizing FNCS', flush=True)
fncs.finalize()
print('done', flush=True)
