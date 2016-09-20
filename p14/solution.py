mp = {}

def go(x):
	if x == 1:
		return 1
	if x not in mp:
		if x % 2 == 0:
			mp[x] = 1 + go(int(x / 2))
		else:
			mp[x] = 1 + go(int(3 * x + 1))
	return mp[x]

result = 1
for i in range(1, 1000000):
	if go(i) > go(result):
		result = i
print(result)
