#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros

while True:
    n = int(input())
    if n == 0:
        break
    h = list(map(int,input().split()))
    h.append(h[0])
    h.append(h[1])
    aux = 0
    for i in range(1, n+1):
        if h[i] < h[i-1] and h[i] < h[i+1]:
            aux += 1
        elif h[i] > h[i-1] and h[i] > h[i+1]:
            aux += 1
    print(aux)
