import sys


#start /b cmd /c python house_controller.py input/controller_registration_F1_house_B0_thermostat_controller.json
		
old_stdout = sys.stdout
log_file = open("IEEE_CFG_180.txt","w")
sys.stdout = log_file
#sys.stdout = old_stdout

for i in range(15):
    for j in range(12):
        print('subscribe "precommit:house_'+str(i+1)+'_'+str(j+1)+'.cooling_setpoint <- house_'+str(i+1)+'_'+str(j+1)+'/house_'+str(i+1)+'_'+str(j+1)+'_cooling_setpoint";')

sys.stdout = old_stdout
log_file.close()
