import sys

for i in range(15):
	for j in range (12):
		old_stdout = sys.stdout
		log_file = open('house_'+str(i+1)+'_'+str(j+1)+'.yaml',"w")
		sys.stdout = log_file
		print('name: house_'+str(i+1)+'_'+str(j+1))
		print('time_delta: 5m')
		print('broker: tcp://localhost:5570')
		print('values:')
		print('    house_'+str(i+1)+'_'+str(j+1)+'_status:')
		print('        topic: DSO/house_'+str(i+1)+'_'+str(j+1)+'_status')
		print('        default: 0.0')
		sys.stdout = old_stdout
		log_file.close()
