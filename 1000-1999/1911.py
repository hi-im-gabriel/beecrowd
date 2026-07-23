#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
#d=dict()
#d[key]=s[value]
#d=dict(sorted(d.items(), key=lambda item: item[1]))

while True:
   n=int(input())
   if n==0:break
   assina=[]
   verifica=[]
   for i in range(n):
      s=input().split()
      assina.append(s[0])
      assina.append(s[1])
   m=int(input())
   falsas=0
   for i in range(m):
      s=input().split()
      aux=assina.index(s[0])
      tam=len(assina[aux+1])
      ver=0
      for j in range(tam):
         if assina[aux+1][j]!=s[1][j]:
            ver+=1
         if ver>1:
            falsas+=1
            break
   print(falsas)
