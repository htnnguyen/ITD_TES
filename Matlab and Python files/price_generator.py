import sys


old_stdout = sys.stdout

log_file = open("prices.txt","w")

sys.stdout = log_file

print ('#time	topic  value')

#sys.stdout = old_stdout



for i in range(56):
    for j in range(60):
        x=(i*60*60+j*60)*1000000000
        if ((i>=0) and (i<9)):
                print(x,' ','clear_price',' ','-0.2')
                #sys.stdout = old_stdout
        elif ((i>12) and (i<20)):
                print(x,' ','clear_price',' ','0.2')
        elif ((i>36) and (i<44)):
                print(x,' ','clear_price',' ','0.2')
        elif ((i>24) and (i<33)):
                print(x,' ','clear_price',' ','-0.2')
            
        else:
                print(x,' ','clear_price',' ','0')
                
        
sys.stdout = old_stdout
log_file.close()
