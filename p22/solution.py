def get_score(x):
	return sum([ord(c) - ord('A') + 1 for c in x])

names = []
with open('names.txt', 'r') as f:
	names = [name[:len(name) - 1] for name in f.readlines()]

names.sort()
result = 0
for i in range(len(names)):
	result += get_score(names[i]) * (i + 1)
print(result)
