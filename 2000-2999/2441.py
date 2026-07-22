f=sorted(list(map(int,input().split())))
x=[i for i in range(601) if i not in range(f[0],f[0]+201) if i not in range(f[1]+1,f[1]+201) if i not in range(f[2]+1,f[2]+201)]
print(len(x)*100)
