n = int(input())

for i in range(n):
    minutos, tempo = input().split()
    minutos = int(minutos)
    total = 0
    if tempo == '2T':
        total += 45
        
    if minutos > 45:
        print(f'{total + 45}+{minutos - 45}')
    else:
        total += minutos
        print(total)
