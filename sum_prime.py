import math
#c is the highest prime in the list
def is_prime(a,primes,c):
	for i in primes:
		if (i> math.sqrt(a)):
			return 1
		if((a%i)==0):
			return 0

	for i in range(c+2,a,2):
		if ((a%i)==0):
			return 0
	return 1

total = 0
primes =[2]

ulo= 600851475143

for i in range(3,int(math.sqrt(ulo)),2):
	 if(is_prime(i,primes,primes[-1])==1):
		primes.append(i)
	

		
# apparently 3 will not miss
total += 2 #for the missing 2
print total 

factor =[]

for i in primes:
	if ((ulo%i)==0):
		factor.append(i)

print factor
