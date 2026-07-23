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
23
24
25
#n= list(map(int,input().split()))
#string.split("+",2)
#import re re.sub("[^0-9]", ", string)
#string.append(input()) array
n=int(input())
while n:
    l=int(input())
    while l:
        k=int(input())
        if k==1:
            print("Rolien")
        elif k==2:
            print("Naej")
        elif k==3:
            print("Elehcim")
        elif k==4:
            print("Odranoel")
        l-=1
    n-=1
