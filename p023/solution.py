BOUND = 30000
not_prime = [False] * (BOUND + 1)
primes = []

for i in range(2, BOUND):
	if not not_prime[i]:
		primes.append(i)
		lim = int(BOUND / i)
		for k in range(i, lim + 1):
			not_prime[i * k] = True

def geometric_sum(r, n):
	return int((1 - r ** (n + 1)) / (1 - r))

def sum_divisors(n):
	original_n = n
	result = 1
	for prime in primes:
		if prime ** 2 > n:
			if n > 1:
				result *= geometric_sum(n, 1)
			break
		count = 0
		while n % prime == 0:
			count += 1
			n /= prime
		result *= geometric_sum(prime, count)
	return result - original_n

LIMIT = 28123
abundant_numbers = []
for i in range(2, LIMIT):
	if sum_divisors(i) > i:
		abundant_numbers.append(i)
good = [False] * (LIMIT + 1)
for i in range(len(abundant_numbers)):
	for j in range(i, len(abundant_numbers)):
		a = abundant_numbers[i]
		b = abundant_numbers[j]
		if a + b <= LIMIT:
			good[a + b] = True
result = 0
for i in range(1, LIMIT + 1):
	if not good[i]:
		result += i
print(result)
