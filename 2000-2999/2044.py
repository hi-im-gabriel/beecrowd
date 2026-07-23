#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)

while True:
    n=int(input())
    p=[]
    if n==-1:
        break
    aux=vis=0
    i=0
    p=list(map(int,input().split()))
    while i<n:
        aux+=p[i]
        if aux%100==0:
            vis+=1
            aux=0
        i+=1
    print(vis)
