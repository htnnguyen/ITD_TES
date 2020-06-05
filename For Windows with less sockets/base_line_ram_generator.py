
import math
import csv
import sys

f = open('base_line.csv','r')
reader = csv.reader(f)
val = []
time = []




for line in reader:
	if(line[0][0] != '#'):
		val.append(float(line[0]))
		
min_val=min(val)
max_val=max(val)

val=[(min_val+(x-min_val)*1.0) for  x in val]
val = [ min(x,max_val) for x in val]

#plt.savefig("test.png",bbox_inches='tight')
#Code to write base_line.txt:
old_stdout = sys.stdout

log_file = open("base_line.txt","w")

sys.stdout = log_file

print ('#time	topic  value')

for i in range(len(val)):
	x = (i*60)*1000000000
	print(x,'	','base_line','	',float(val[i]))

sys.stdout = old_stdout
log_file.close()
