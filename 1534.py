while True:
    try:
        n=int(input())
        m=[]
        for i in range(n):
            m.append([])
            for j in range(n):m[i].append('3')
            aux=n-1
        for i in range(n):
            m[i][i]='1'
            m[i][aux]='2'
            aux-=1
            print(*m[i],sep="")
    except EOFError:break
