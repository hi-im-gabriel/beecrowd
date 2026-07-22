f,b = [],[]
n=int(input())
for i in range(n):f.append(list(map(int,input().split())))
for i in range(n*2):
    x,y=map(int,input().split())
    b.append(f[x-1][y-1])
print(len(set(b)))
