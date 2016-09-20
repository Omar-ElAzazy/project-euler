BOUND = 1000000
not_prime = [False] * (BOUND + 1)
primes = []

for i in range(2, BOUND):
	if not not_prime[i]:
		primes.append(i)
		lim = int(BOUND / i)
		for k in range(i, lim + 1):
			not_prime[i * k] = True

def count_divisors(n):
	result = 1
	for prime in primes:
		if prime ** 2 > n:
			if n > 1:
				result *= 2
			break
		count = 0
		while n % prime == 0:
			count += 1
			n /= prime
		result *= (count + 1)
	return result

num = 1
i = 1
N = 500
while count_divisors(num) <= N:
	i += 1
	num += i
print(num)	
