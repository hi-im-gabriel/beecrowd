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

s=input()
tam=len(s)
f=""
aux=0
for i in range(tam):
   if aux==1:
      aux=0
      continue
   if s[i]=='p':
      try:
         f+=s[i+1]
      except:
         continue
      aux=1
   else:
      f+=s[i]
print(f)
