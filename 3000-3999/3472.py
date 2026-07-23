1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
criancas = int(input())
silabas = 29
arr = [1, 1]
for _ in range(criancas - 1):
    arr.extend([1, 1]) 
idx = 0
restantes = sum(arr)
while restantes > 1:
    count = 0
    while count < silabas:
        if arr[idx % len(arr)] == 1:
            count += 1
        idx += 1
    elim_idx = (idx - 1) % len(arr)
    arr[elim_idx] = 0
    restantes -= 1
    while arr[idx % len(arr)] == 0:
        idx += 1
winner = arr[0] == 1 or arr[1] == 1
print("vai ganhar" if winner else "nao vai ganhar")
