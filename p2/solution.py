N = 4000000
result = 0
f1 = 1
f2 = 2
while f2 <= N:
	if f2 % 2 == 0:
		result += f2
	f1, f2 = f2, f1 + f2
print(result)
