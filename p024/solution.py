factorial = [1] * 11
for i in range(1, 11):
	factorial[i] = factorial[i - 1] * i

def get_nth_permutation(n):
	n -= 1
	nums = [x for x in range(10)]
	result = ''
	for i in range(10):
		ind = int(n / factorial[9 - i])
		added = nums[ind]
		nums.remove(added)
		result += str(added)
		n -= ind * factorial[9 - i]
	return result

print(get_nth_permutation(1000000))
