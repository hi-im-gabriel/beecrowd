#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)

def conta(n):
    aux=[1,1,2]
    i=3
    while i<=n:
        aux.append((((aux[i - 1] + aux[i - 2]) % 1000000007 + aux[i - 3]) % 1000000007) % 1000000007)
        i+=1
    return aux[n];

n=int(input())
print(conta(n))
