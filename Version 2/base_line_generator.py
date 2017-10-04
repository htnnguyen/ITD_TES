
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
