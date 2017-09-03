import sys


##old_stdout = sys.stdout
##log_file = open("IEEE_FNCS_CFG.txt","w")
##sys.stdout = log_file
###sys.stdout = old_stdout
##
##for i in range(15):
##    for j in range(12):
##        message='subscribe "precommit:house_'+str(i+1)+'_'+str(j+1)+'.cooling_system_type <- house_'+str(i+1)+'_'+str(j+1)+'/cooling_system_type"' 
##        print(message)
##
##for i in range(15):
##    for j in range(12):
##        message='subscribe "precommit:house_'+str(i+1)+'_'+str(j+1)+'.cooling_mode <- house_'+str(i+1)+'_'+str(j+1)+'/cooling_mode"' 
##        print(message)
##
##sys.stdout = old_stdout
##log_file.close()


#start /b cmd /c python house_controller.py input/controller_registration_F1_house_B0_thermostat_controller.json
		

old_stdout = sys.stdout
log_file = open("180agents_bat.txt","w")
sys.stdout = log_file
#sys.stdout = old_stdout

for i in range(15):
    for j in range(12):
        print('set FNCS_CONFIG_FILE=house_'+str(i+1)+'_'+str(j+1)+'.yaml')
        message='start /b cmd /c python house_controller.py house_'+str(i+1)+'_'+str(j+1)+' ^>house_controller'+str(i+1)+'_'+str(j+1)+'.log 2^>^&1'
        print(message)

sys.stdout = old_stdout
log_file.close()
