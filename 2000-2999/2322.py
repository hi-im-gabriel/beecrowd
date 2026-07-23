#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa


n=int(input())
lista=list(map(int,input().split()))
lista.sort()
for i in range(len(lista)):
    if lista[i]!=(i+1):
        break
if lista[i]==(i+1):
    i+=1
print(i+1)
