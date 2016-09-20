f1, f2 = 1, 1
index = 1
while len(str(f1)) < 1000:
	f1, f2 = f2, f1 + f2
	index += 1
print(index)
