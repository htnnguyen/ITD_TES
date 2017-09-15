import sys
import yaml

#start /b cmd /c python house_controller.py input/controller_registration_F1_house_B0_thermostat_controller.json
		
#old_stdout = sys.stdout
#log_file = open("AuctionYaml.yaml","w")
#sys.stdout = log_file
#sys.stdout = old_stdout

data = {}

for i in range(15):
    for j in range(12):
        housename = 'house_'+str(i+1)+'_'+str(j+1)+'_thermostat_controller'
        details = {'topic':'controller_house_'+str(i+1)+'_'+str(j+1)+'_thermostat_controller/TransactiveAgentOutput', 'default': {"controller":{"house_"+str(i+1)+'_'+str(j+1):{"bid_id":{"propertyType":"string","propertyUnit":"none","propertyValue":0},"market_id":{"propertyType":"integer","propertyUnit":"none","propertyValue":0},"price":{"propertyType":"double","propertyUnit":"none","propertyValue":0.0},"quantity":{"propertyType":"double","propertyUnit":"none","propertyValue":0.0},"rebid":{"propertyType":"integer","propertyUnit":"none","propertyValue":0},"state":{"propertyType":"string","propertyUnit":"none","propertyValue":"ON"},"air_temperature": {"propertyType": "double", "propertyUnit": "none", "propertyValue": 0.0}}}}}
        #d = {housename:details}
        data[housename] = details
        #print('house_'+str(i+1)+'_'+str(j+1)+'_thermostat_controller:')
        #print('topic: controller_house_house_'+str(i+1)+'_'+str(j+1)+'_thermostat_controller/TransactiveAgentOutput')
        #print('default: {"controller":{"house_'+str(i+1)+'_'+str(j+1)+'":{"bid_id":{"propertyType":"string","propertyUnit":"none","propertyValue":0},"market_id":{"propertyType":"integer","propertyUnit":"none","propertyValue":0},"price":{"propertyType":"double","propertyUnit":"none","propertyValue":0.0},"quantity":{"propertyType":"double","propertyUnit":"none","propertyValue":0.0},"rebid":{"propertyType":"integer","propertyUnit":"none","propertyValue":0},"state":{"propertyType":"string","propertyUnit":"none","propertyValue":"ON"},  "air_temperature": {"propertyType": "double", "propertyUnit": "none", "propertyValue": 0.0}}}}')

with open('AuctionYaml.yaml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)

#sys.stdout = old_stdout
#log_file.close()
