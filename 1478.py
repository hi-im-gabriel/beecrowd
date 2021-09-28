while True:
    N=int(input())
    if N==0:break
    f=[]
    for i in range(1,N+1):
        aux=[]
        c=i
        for j in range(N):
            aux.append(abs(c))
            if c==1:c-=3
            else:c-=1
        f.append(aux)
    for i in range(N):
        s=''
        for j in range(N):s+=" %3d"%f[i][j]
        print(s[1:])
    print("")
