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
#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
f = []
spent = []
f_count = 0
dias = int(input())
for i in range(dias):        
    spent.append(float(input()))
    f.append(input().split())
for dia in range(len(f)):
    f_count+=len(f[dia])
    print("day {}: {} kg".format(dia+1, len(f[dia])))    
print("{} kg by day".format(round(f_count/dias, 2)))
print("R$ {} by day".format(round(sum(spent)/dias, 2)))
