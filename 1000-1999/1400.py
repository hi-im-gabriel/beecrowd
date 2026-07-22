def res(n):
    ascending,aux=True,0
    while True:    
        if aux==1:ascending=True
        elif aux==n:ascending=False
        if ascending:aux+=1
        else:aux-=1
        yield aux
def palma(n, m, k):
    aux,aux2,palmas,i=res(n),0,0,1
    while True:
        aux2=aux.__next__()
        if aux2==m:
            if i%7==0 or '7' in str(i):palmas+=1
            if palmas==k:return i
        i+=1
while True:
    n,m,k=map(int, input().split())
    if n==m==k==0:break
    print(palma(n,m,k))
