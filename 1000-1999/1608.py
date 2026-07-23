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
#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
for g in range(int(input())):
   d, i, b = [int(x) for x in input().split()]
   ind = [int(x) for x in input().split()]
   bolos = [0 for x in range(b)]
   for j in range(b):
      e = [int(x) for x in input().split()][1:]
      bolos[j] = 0
      for k in range(0, len(e), 2):
         bolos[j] += ind[e[k]] * e[k+1]
   print(d // min(bolos))
