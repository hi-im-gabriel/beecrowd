n = int(input())
m = int(input())

figurinha = [0] * n

while m:
    m -= 1
    figurinha[int(input()) - 1] = 1
x = figurinha.count(0)
print(x)
