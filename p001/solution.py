N = 1000
count_3 = int(N / 3) - (N % 3 == 0)
count_5 = int(N / 5) - (N % 5 == 0)
count_15 = int(N / 15) - (N % 15 == 0)

sum_3 = int(count_3 * (3 + count_3 * 3) / 2)
sum_5 = int(count_5 * (5 + count_5 * 5) / 2)
sum_15 = int(count_15 * (15 + count_15 * 15) / 2) 

result = sum_3 + sum_5 - sum_15
print(result)
