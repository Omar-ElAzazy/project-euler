def gcd(a, b):
	while b:
		a, b = b, a % b
	return a	

def lcm(a, b):
	return a * b / gcd(a, b)

N = 20
result = 1
for i in range(2, N + 1):
	result = lcm(result, i)
print(int(result))
