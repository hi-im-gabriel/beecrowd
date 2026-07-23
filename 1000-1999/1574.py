#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
for i in range(int(input())):
    n=int(input())
    aux=[]
    p=0
    for i in range(n):
        s=list(map(str,input().split()))
        if len(s)==1:
            aux.append(s[0])
            if s[0]=="LEFT":
                p-=1
            elif s[0]=="RIGHT":
                p+=1
        else:
            i=int(s[2])
            if aux[i-1]=="LEFT":
                p-=1
                aux.append(aux[i-1])
            elif aux[i-1]=="RIGHT":
                p+=1
                aux.append(aux[i-1])
    print(p)
