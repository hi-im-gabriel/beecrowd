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
n = int(input())
m = int(input())
figurinha = [0] * n
while m:
    m -= 1
    figurinha[int(input()) - 1] = 1
x = figurinha.count(0)
print(x)
