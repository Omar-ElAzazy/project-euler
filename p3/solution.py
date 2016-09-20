N = 600851475143
result = 1
i = 2
while i < (N + 1) ** 0.5:
	if N % i == 0:
		result = i
		while N % i == 0:
			N /= i
	i = i + 1
result = max(result, N)
print(int(result))
