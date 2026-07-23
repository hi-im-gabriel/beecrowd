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
def x(n):
   if n%3==0:return True
   return False
while True:
   try:
      n,c=map(int,input().split())
      aux=0
      while c:
         aux+=int((c%10))
         c=int(c/10)
      print(int(aux),end=" ")
      print("sim") if x(aux) else print("nao")
   except EOFError:break
