import os
for i in range(15):
	for j in range(12):
		#houseID[i][j]=
		os.remove('house_'+str(i+1)+'_'+str(j+1)+'.csv')
		os.remove('house_controller'+str(i+1)+'_'+str(j+1)+'.log')
		os.remove('house_'+str(i+1)+'_'+str(j+1)+'.yaml')
