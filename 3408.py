from re import sub

N = int(input())
soma = 0

for _ in range(N):
    soma += int(sub(r'[A-Z]', '', input()))
   
print(soma)
