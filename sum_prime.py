#c is the highest prime in the list
def is_prime(a,primes,c):
	for i in primes:
		if((a%i)==0):
			return 0

	for i in range(c+2,a,2):
		print i
		if ((a%i)==0):
			return 0
	return 1

total = 0
primes =[2]

for i in range(3,200,2):
	 if(is_prime(i,primes,primes[-1])==1):
		primes.append(i)
		total += i

		
# apparently 3 will not miss
total += 2 #for the missing 2
print total 

