def dodo(n):
    return (n*(n-1))/2

def quaqua(n):
    return (n*(n-1)*(n-2)*(n-3))/(4*3*2)

n=int(input())

print(int(1+dodo(n)+quaqua(n)))
