n, m = map(int, input().split())
run = {}
for i in range(n):
    c, x = input().split()
    run[c] = int(x)

aux = 0

x = int(input())

s = input().split()

for c in s:
    aux += run[c]

print(aux)
print("You shall pass!") if aux >= m else print("My precioooous")
