for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>b:a,b=b,a
    soma=0
    for i in range(a+1,b):
        if i%2!=0:soma+=i
    print(soma)
