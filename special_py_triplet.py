import math
list_a =[]

for i in range(1,1001): #end number for triplet
	for u in range(i,1001):
		a = (i**2) + (u**2)
		if (math.sqrt(float(a)).is_integer()):
			list_b =[i,u,math.sqrt(a)]
			list_a.append(list_b) 

for i in list_a:
	if (i[0]+i[1]+i[2] == 1000):
		print(i)
