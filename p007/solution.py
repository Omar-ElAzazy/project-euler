BOUND = 1000000
not_prime = [False] * BOUND
rem = 10001
result = 0

for i in range(2, BOUND):
	if not not_prime[i]:
		rem = rem - 1
		if rem == 0:
			result = i
			break
		lim = int(BOUND / i)
		for k in range(2, lim):
			not_prime[i * k] = True
print(result)
