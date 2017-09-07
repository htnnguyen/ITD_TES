#import matplotlib.pyplot as plt
import random

class hvac:
	def __init__(self, error, houses):
		self.error = error
		self.houses = houses
		self.indexlist = []
		self.valueslist = []
		self.indexsublist = []
		self.valuessublist = []
		self.number_houses = 0
		self.price = 0

	def hvac_number_houses(pval_per_unit):
		self.number_houses = error/pval_per_unit
	
	#Sorting Dictionary
	def hvac_sort_houses(price, node, ta, tb):
		sortedlist = sorted(enumerate(price[node]), key = lambda x: x[1])
		#indexlist = []
		#valueslist = []
		#indexsublist = []
		#valuessublist = []
		for i in sortedlist:
			self.indexlist.append(i[0])
			self.valueslist.append(i[1])
		for i in sortedlist:
			if i[1] >= ta and i[1] <= tb:
				self.valuessublist.append(i[1])
				self.indexsublist.append(i[0])
		#return [valueslist, indexlist, valuessublist, indexsublist]

	def hvac_price_function():#(valueslist, indexlist, valuessublist, indexsublist):
		temp = self.valueslist[n-1]
		if temp < self.valuessublist[0]:
			self.price = 0
			#return 0
		elif temp > self.valuessublist[0] and temp < self.valuessublist[-1]:
			self.price = temp
			#return temp
		else:
			self.price = self.valuessublist[-1]
			#return self.valuessublist[-1]
		

#Testbench:
# price = [[] for i in range(16)]
# for i in range(16):
	# l = []
	# for j in range(12):
		# l.append(random.randint(-20,20))
	# price[i] = l
# print("Price list:")
# print(price)
# print("Sorted lists and sublists: ")
# [l1, l2, l3, l4] = hvac_sort_houses(price, 0, 0, 10)
# print([l1, l2, l3, l4])
# print("Price:")
# print(hvac_price_function(l1, l2, l3, l4, 8))