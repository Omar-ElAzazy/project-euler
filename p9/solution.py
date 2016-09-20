def get_c(b):
	return int((5 * 10**5 - 1000 * b + b * b) / (1000 - b))
def get_a(b, c):
	return 1000 - b - c

ra, rb, rc = 0, 0, 0
for b in range(1, 1000):
	c = get_c(b)
	a = get_a(b, c)
	if a * a + b * b == c * c:
		ra, rb, rc = a, b, c
		break
print(ra * rb * rc)
