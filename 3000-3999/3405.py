N = int(input())

count_zeros = 0
divisor = 5

while divisor <= N:
    count_zeros += N // divisor
    divisor *= 5

print(count_zeros)
