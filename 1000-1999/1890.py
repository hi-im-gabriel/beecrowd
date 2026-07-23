#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

for i in range(int(input())):
    x,y=map(int,input().split())
    if x==y==0:
        print("0")
    elif x==0 and y!=0:
        print(pow(10,y))
    elif y==0 and x!=0:
        print(pow(26,x))
    else:
        print(pow(10,y)*pow(26,x))
