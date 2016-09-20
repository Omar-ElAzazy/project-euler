def sum_of_squares(n):
	return n ** 3 / 3 + n ** 2 / 2 + n / 6

def arithmetic_sum(n):
	return n * (1 + n) / 2

N = 100
result = arithmetic_sum(N) ** 2 - sum_of_squares(N)
print(int(result))
