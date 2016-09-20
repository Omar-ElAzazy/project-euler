result = 0
for a in range(111, 1000):
	for b in range(a, 1000):
		p = a * b
		if str(p) == str(p)[::-1]:
			result = max(result, p)
print(result)
