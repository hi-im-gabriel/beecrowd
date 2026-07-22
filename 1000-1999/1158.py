for _ in range(int(input())):
    a,b=map(int,input().split())
    if a%2==0:a+=1
    x=[]
    while len(x)!=b:
        x.append(a)
        a+=2
    print(sum(x))
