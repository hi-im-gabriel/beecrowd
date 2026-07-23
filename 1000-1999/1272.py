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
21
22
#n= list(map(int,input().split()))
#string.split('+',2)
#import re re.sub("[^0-9]",""", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")
n=int(input())
while n:
    nome=[]
    string=input().split()
    tam=len(string)-1
    i=0
    while i<=tam:
        nome.append(string[i][0])
        i+=1
    print(*nome,sep="")
    n-=1
