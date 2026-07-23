1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
acertos=["azar"]*3
acertos+=["terno","quadra","quina","sena"]
aposta=list(map(int,input().split()))
sorteio=list(map(int,input().split()))
aux=0
for i in range(6):
    if aposta[i] in sorteio:
        aux+=1
print(acertos[aux])
