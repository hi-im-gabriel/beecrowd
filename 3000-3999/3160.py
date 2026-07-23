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
L = input().split()
N = input().split()
S = input()
if S == "nao":
    result = L + N
else:
    idx = L.index(S)
    result = L[:idx] + N + L[idx:]
print(" ".join(result))
