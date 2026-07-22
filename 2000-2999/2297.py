teste=1
while True:
    n=int(input())
    if n==0:break
    aldo=beto=0
    for i in range(n):
        a,b=map(int,input().split())
        aldo+=a
        beto+=b
    venc="Aldo" if aldo>beto else "Beto"
    print(f"Teste {teste}\n{venc}\n")
    teste+=1
