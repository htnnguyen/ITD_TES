""" ][]\][]
This file simulates a controller object
"""
import warnings
import sys
import json
import fncs

# Class definition
class ramp_controller_objectNew:
    
    # ====================Define instance variables ===================================
    def __init__(self, controllerDict):
        
        # Obtain the registration data and initial values data
        agentRegistration = controllerDict['registration']
        agentInitialVal = controllerDict['initial_values']
        
        # Initialize the variables
        self.market = {'name': 'none', 'market_id': 0, 'average_price': -1, 'std_dev': -1, 'clear_price': -1, \
          'initial_price': -1, 'price_cap':9999.0, 'period': -1}   
        
        self.house = {#'target': 'air_temperature', 'setpoint0':-1, 'lastsetpoint0': 0, 'controlled_load_all': 1, 'controlled_load_curr': 1, \
         'deadband': 0, 'currTemp': -1, # 'uncontrolled_load': 1, 'deadband': 0, 'powerstate': 'UNKNOWN', 'last_pState': 'UNKNOWN', 
         # 'thermostat_state': 'UNKNOWN', 
         # 're_override': 'NORMAL', \
         'houseType': 'Unknown', 'thermostatcontrol': 'UNKNOWN', 'systemmode': 'UNKNOWN', 'last_systemmode': 'UNKNOWN', 'Tbliss': 0, 'd': 1, 'theta': 1, 'P': 1 
         }
        
        self.controller = {'name': 'none','marketName': 'none', 'houseName': 'none', 'simple_mode': 'none', 'setpoint': 'none', 'lastbid_id': -1, 'lastmkt_id': -1, 'bid_id': 'none', \
              'deadband': 0, 'period': -1, #'slider_setting': -0.001, 'ramp_low': 0, 'ramp_high': 0, 'range_low': 0, \
              # 'range_high': 0, 'dir': 0, 'direction': 0, 'use_predictive_bidding': 0, 'deadband': 0, 'last_p': 0, \
              'last_q': 0, 'setpoint0': -1, 'minT': 0, 'maxT': 0, 'bid_delay': 60, 'next_run': 0, 't1': 0, 't2': 0, 
              # 'use_override': 'OFF', 'control_mode': 'CN_RAMP', 'resolve_mode': 'DEADBAND', 
              'sliding_time_delay': -1, 
              'thermostat_mode': 'INVALID',  'last_mode': 'INVALID', 'previous_mode': 'INVALID',
              'time_off': sys.maxsize
              }
        
        self.controller_bid = {'market_id': -1, 'bid_id': 'none', 'bid_price': 0.0, 'bid_quantity': 0, 'bid_accepted': 1, \
                               'state': 'UNKNOWN', 'rebid': 0}
      
      
        self.controller['name'] = agentRegistration['agentName']

        # Read and assign initial values from agentInitialVal
        # controller information
        self.controller['control_mode'] = agentInitialVal['controller_information']['control_mode']
        self.controller['marketName'] = agentInitialVal['controller_information']['marketName']
        self.controller['houseName'] = agentInitialVal['controller_information']['houseName']
        self.controller['bid_id'] = agentInitialVal['controller_information']['bid_id']
        self.controller['period'] = agentInitialVal['controller_information']['period']
        self.controller['last_setpoint'] = self.controller['setpoint0']
        
        # market information - Market registration information
        self.market['name'] = self.controller['marketName']
        self.market['market_id'] = agentInitialVal['market_information']['market_id']
        self.market['market_unit'] = agentInitialVal['market_information']['market_unit']
        self.market['initial_price'] = agentInitialVal['market_information']['initial_price']
        self.market['average_price'] = agentInitialVal['market_information']['average_price']
        self.market['std_dev'] = agentInitialVal['market_information']['std_dev']
        self.market['clear_price'] = agentInitialVal['market_information']['clear_price']
        self.market['price_cap'] = agentInitialVal['market_information']['price_cap']
        self.market['period'] = agentInitialVal['market_information']['period']
        
        # house information  - values will be given after the first time step, thereforely here set as default zero values
        self.house['currTemp'] = 78
        self.house['powerstate'] = "ON"
        self.house['controlled_load_all'] = 0 
        self.house['target'] = "air_temperature"
        self.house['deadband'] = 2 
        self.house['setpoint0'] = 0
        self.house['lastsetpoint0'] = self.house['setpoint0']
        
        self.house['thermostatcontrol'] = "NONE"
        self.house['systemmode'] = "COOL"
        self.house['last_systemmode'] = self.house['systemmode']
        # from auctionDict initial_values
        self.house['Tbliss'] = agentInitialVal['house_information']['Tbliss']
        self.house['d'] = agentInitialVal['house_information']['d']
        self.house['theta'] = agentInitialVal['house_information']['theta']
        self.house['P'] = agentInitialVal['house_information']['P']
        self.house['houseType'] = agentInitialVal['house_information']['houseType']

        # Generate agent publication dictionary
        self.fncs_publish = {
            'controller': {
                self.controller['name']: {
                    'market_id': {'propertyType': 'integer', 'propertyUnit': '', 'propertyValue': 0},
                    'bid_id': {'propertyType': 'string', 'propertyUnit': '', 'propertyValue': 0},
                    'bid_name': {'propertyType': 'string', 'propertyUnit': '', 'propertyValue': 'none'},
                    'price': {'propertyType': 'double', 'propertyUnit': '', 'propertyValue': 0.0},
                    'quantity': {'propertyType': 'double', 'propertyUnit': '', 'propertyValue': 0.0},
                    'bid_accepted': {'propertyType': 'integer', 'propertyUnit': '', 'propertyValue': 1},
                    'state': {'propertyType': 'string', 'propertyUnit': '', 'propertyValue': 'BS_UNKNOWN'},
                    'rebid': {'propertyType': 'integer', 'propertyUnit': '', 'propertyValue': 0},
                    'air_temperature': {'propertyType': 'double', 'propertyUnit': '', 'propertyValue': 78}
                    }
                }
            } 
        
        # Registrate the agent      
        agentRegistrationString = json.dumps(agentRegistration)
        self.fncs_publish['controller'][self.controller['name']]['air_temperature'] = self.house['currTemp']
        fncs.agentRegister(agentRegistrationString.encode('utf-8'))
        print('agent registration is done', flush = True)

    # ====================extract float from string ===============================
    def get_num(self,fncs_string):
        return float(''.join(ele for ele in fncs_string if ele.isdigit() or ele == '.'))
        
    def get_number(self,value):
        return float(''.join(ele for ele in value if ele.isdigit() or ele == '.'))
            # ====================Obtain values from the broker ===========================
    def subscribeGLD(self, title, value):    
        if title.startswith('air_temperature'):
            print('In subscribeVal air_temperature??', title, value, flush=True)
            self.house['currTemp'] = self.get_number(value)
            self.fncs_publish['controller'][self.controller['name']]['air_temperature'] = self.house['currTemp']
        
    # ====================Obtain values from the broker ===========================
    def subscribeVal(self, fncs_sub_value_String):    
        
        # Update market and house information at this time step from subscribed key values:  
        print('fncs_sub_value_String', fncs_sub_value_String, flush = True)
        if "auction" in fncs_sub_value_String:
            self.market['market_id'] = fncs_sub_value_String['auction'][self.market['name']]['market_id']['propertyValue']
            self.market['average_price'] = fncs_sub_value_String['auction'][self.market['name']]['average_price']['propertyValue']
            self.market['std_dev'] = fncs_sub_value_String['auction'][self.market['name']]['std_dev']['propertyValue']
            self.market['clear_price'] = fncs_sub_value_String['auction'][self.market['name']]['clear_price']
            self.market['price_cap'] = fncs_sub_value_String['auction'][self.market['name']]['price_cap']['propertyValue']
            self.market['initial_price'] = fncs_sub_value_String['auction'][self.market['name']]['initial_price']['propertyValue']
            print('In subscribeVal auction', flush = True)
    
    
    # ====================Rearrange object based on given initial values======================  
    def initController(self):
            
        # Update controller bidding period:
        if self.controller['period'] == 0.0:
            self.controller['period'] = 300
        
        # Intialize controller next_run time as the starting time
        self.controller['next_run'] = 0
        
        # Intialize the controller last time price and quantity 
        self.controller['last_p'] = self.market['initial_price']
        self.controller['last_q'] = 0
        
    # ==================================Presync content===========================  
    def presync(self):   
        
        return sys.maxsize
    
    # ==================================Sync content===========================  
    def sync(self, timeSim):    
        
        # Update controller t1 information
        self.controller['t1'] = timeSim
        
        # Inputs from market object:
        marketId = self.market['market_id']
        clear_price = self.market['clear_price']
        avgP = self.market['average_price']
        stdP = self.market['std_dev']
        
        # Inputs from controller:
        
        # Inputs from house object:
        demand = self.house['controlled_load_all']
        monitor = self.house['currTemp']
        powerstate = self.house['powerstate']
        thermostatcontrol = self.house['thermostatcontrol']
        systemmode = self.house['systemmode']
        lastmkt_id = self.controller['lastmkt_id']
        
        air_temperature = self.house['currTemp']
        Tbliss = self.house['Tbliss']
        theta = self.house['theta']
        d = self.house['d']
        P = self.house['P']

        print ("  sync:", demand, powerstate, clear_price, flush=True)
        
        
        if  self.controller['t1'] < self.controller['next_run'] and marketId == lastmkt_id :
            if self.controller['t1'] <= self.controller['next_run'] - bid_delay :
                if self.controller['use_predictive_bidding'] == 1 and ((self.controller['control_mode'] == 'CN_RAMP' and setpoint0 != last_setpoint) or (self.controller['control_mode'] == 'CN_DOUBLE_RAMP' and (self.controller['heating_setpoint0']  != self.controller['last_heating_setpoint'] or self.controller['cooling_setpoint0']  != self.controller['last_cooling_setpoint']))):
                    # Base set point setpoint0 is changed, and therefore sync is needed:
                    pass
                elif self.controller['use_override'] == 'ON' and self.controller['t1'] == self.controller['next_run']- bid_delay :
                    # At the exact time that controller is operating, therefore sync is needed:
                    pass
                else:
                    if self.house['last_pState'] == powerstate:
                        # If house state not changed, then do not go through sync part:
                        return self.controller['next_run']
            else:
                return self.controller['next_run']
        
        # Update house last power state
        self.house['last_pState'] = powerstate
        
        print('checking theta', theta, flush=True)
        print('air_temperature', air_temperature, flush=True)
        print('clear_price', clear_price, flush=True)
        pi = theta * air_temperature
        print('pi*:', pi, theta * air_temperature, flush=True)
        if air_temperature >= Tbliss + d:
            print('air_temperature exceeded Tmax: setting Cool ON for the house', flush=True)
            systemmode = "COOL"
        elif Tbliss - d >= air_temperature:
            print('air_temperature is below Tmin: setting Cool OFF for the house', flush = True)
            systemmode = "OFF"
        elif clear_price > theta * air_temperature:
            print('pi* is below clear_price: setting Cool OFF for the house', flush = True)
            systemmode = "OFF"
        else: 
            print('pi* is above clear_price: setting Cool ON for the house', flush = True)
            systemmode = "COOL"
        fncs.publish('system_mode', systemmode)
        print('publishing set values', flush = True)
        fncs_publishString = json.dumps(self.fncs_publish)
        fncs.agentPublish(fncs_publishString)
        # Return sync time t2
        return sys.maxsize
    
    # ==================================Postsync content===========================   
    def postsync(self):     
        # Update last setpoint if setpoint0 changed
             
        # Compare t1 with next_run to determine the return time stamp heating_setpoint0
        if self.controller['t1'] < self.controller['next_run'] - self.controller['bid_delay']:
            postsyncReturn = self.controller['next_run'] - self.controller['bid_delay']
            return postsyncReturn
        
        if self.controller['t1'] - self.controller['next_run'] < self.controller['bid_delay']:
            postsyncReturn = self.controller['next_run']
        
        if self.controller['t1'] == self.controller['next_run']:
            self.controller['next_run'] += self.controller['period']
            postsyncReturn = self.controller['next_run'] - self.controller['bid_delay']
        
        return postsyncReturn
        
     
            
            
            
        
        
        
        
        
        
        
        