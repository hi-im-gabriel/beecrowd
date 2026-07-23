def binary_search(target, size):
    low = 0
    high = size - 1

    while high > low:
        mid = low + (high - low) // 2
        if vet[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low

n = int(input())
vet = []

soma_total = 0
soma = 0

tmp_list = list(map(int, input().split()))
vet.append(tmp_list[0])
soma_total += vet[0]

for i in range(1, n):
    vet.append(vet[i - 1] + tmp_list[i])
    soma_total += tmp_list[i]

print(binary_search(soma_total // 2, n) + 1)
