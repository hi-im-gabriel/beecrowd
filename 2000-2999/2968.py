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
20
#n= list(map(int,input().split()))
import math
a,b=input().split()
a=int(a)
b=int(b)
total=a*b
aux=[]
for i in range(1,10):
    perc=i/10
    qtd=total*perc
    qtd_str=str(math.ceil(qtd))
    aux.append(qtd_str)
res_str= " ".join(aux)
print(res_str)
