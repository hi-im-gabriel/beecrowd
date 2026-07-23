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
#n= list(map(int,input().split()))
#string.split("+",2)
#import re re.sub("[^0-9]", ", string)
#string.append(input()) array
while True:
    n=int(input())
    j1=j2=0
    if n==0:
        break
    while n:
        a,b=input().split()
        a=int(a)
        b=int(b)
        if a>b:
            j1+=1
        elif b>a:
            j2+=1
        n-=1
    print("%d %d" % (j1,j2))
