BOUND = 2000000
not_prime = [False] * (BOUND + 1)
result = 0
for i in range(2, BOUND):
	if not not_prime[i]:
		result += i
		lim = int(BOUND / i)
		for k in range(2, lim + 1):
			not_prime[i * k] = True
print(result)

