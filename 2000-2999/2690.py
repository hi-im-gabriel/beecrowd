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
18
19
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
x=['GQaku', 'ISblv', 'EOYcmw', 'FPZdnx', 'JTeoy', 'DNXfpz', 'AKUgq', 'CMWhr', 'BLVis', 'HRjt']
for i in range(int(input())):
   s=input().replace(' ','')
   f=''
   for c in s:
      f+=str([i for i, new in enumerate(x) if c in new][0])
      if len(f)==12:break
   print(f)
