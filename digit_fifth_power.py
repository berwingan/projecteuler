


total = 0


def pizza(a):
	b = str(a)
	check = 0
	for i in range(len(b)):
		check += (int(b[i])**5)
	if (check==a):
		return a
	return 0

for i in range(2,1000000):
	 total += pizza(i)

print total
