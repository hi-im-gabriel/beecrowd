#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
teste=1
def res(par,impar):
    if (par+impar)%2==0:
        return True

while True:
    n = int(input())
    nome=[]
    if n == 0:break
    nome.append(input())
    nome.append(input())
    print(f"Teste {teste}")
    for i in range(n):
        par,impar=map(int,input().split())
        print(nome[0]) if res(par,impar) else print(nome[1])
    print()
    teste+=1
