global s
s = 0
def exp(p, k):
    r = 1
    for i in range(0, k):
        r *= p
    return r

for _ in range(int(input())):
    n, p, i = input().split()
    n = int(n)
    p = float(p)
    i = int(i)
    pn = exp(1 - p, n)
    pi = exp(1 - p, i - 1)
    r = pi

    for j in range(10000):
        pi *= pn
        r += pi
    
    print(f'{r*p:.4f}')
