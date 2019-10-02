def num_at(li,a):
	run = ""
	for i in range(1,a):
		run += str(i)
	count = 1
	for i in li:
		count *= int(run[i-1])
	return count



li =[1,10,100,1000,10000,100000,1000000]
b  = num_at(li,1000000)

print(b)
