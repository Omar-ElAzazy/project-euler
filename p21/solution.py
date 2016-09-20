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


sum_divisors_cache = [0] * (BOUND + 1)
for i in range(1, 10000):
	sum_divisors_cache[i] = sum_divisors(i)

def is_amicable_number(x):
	y = sum_divisors_cache[x]
	return y < 10000 and x != y and sum_divisors_cache[y] == x

result = 0
for i in range(1, 10000):
	if is_amicable_number(i):
		result += i
print(result)
