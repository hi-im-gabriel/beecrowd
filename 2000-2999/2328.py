#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)


divisoes = int(input())
x = 0
pedacos = list(map(int,input().split()))

for i in pedacos:
    x += i

y = x-divisoes
print(y)
