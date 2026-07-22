for t in range(int(input())):
    n,m=map(int,input().split())
    f=[]
    for i in range(n):
        nome,peso,idade,altura=input().split()
        x=[nome,int(peso),int(idade),float(altura)]
        f.append(x)
    f=sorted(f,key=lambda x: x[0])
    f=sorted(f,key=lambda x: x[3])
    f=sorted(f,key=lambda x: x[2])
    f=sorted(f,key=lambda x: x[1],reverse=True)
    print("CENARIO {%d}"%(t+1))
    for j in range(m):
        print(f"{j+1} - {f[j][0]}")
