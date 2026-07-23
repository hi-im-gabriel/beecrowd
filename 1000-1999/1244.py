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
#n= list(map(int,input().split()))
#string.split("+",2)
#import re re.sub("[^0-9]", ", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")
n=int(input())
while n:
    s=input().split()
    #qtd=len(s)-1
    s=sorted(s,key=len,reverse=True)
    tam=len(s)
    print(*s,sep=" ")
    n-=1
