L = input().split()
N = input().split()
S = input()

if S == "nao":
    result = L + N
else:
    idx = L.index(S)
    result = L[:idx] + N + L[idx:]

print(" ".join(result))
