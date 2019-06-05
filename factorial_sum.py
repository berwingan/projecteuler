j = 100

a = 1
for i in range(1,j+1):
	a *= i
	print(a)

b = str(a)
c = 0
for i in b:	
	c += int(i)


print(c)	 
