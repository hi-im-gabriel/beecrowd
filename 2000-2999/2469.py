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
from collections import Counter
n = int(input())

notas=list(map(int,input().split()))
freq=Counter(notas)
freq=dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))
for i,j in freq.items():
   aux=j
   break
final=[]
for i,j in freq.items():
   if j==aux:
      final.append(i)
   else:
      break
print(max(final))
