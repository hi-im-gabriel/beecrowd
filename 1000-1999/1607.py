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
#n= list(map(int,input().split()))
#string.split("+",2)
#import re re.sub("[^0-9]", ", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")
n = int(input())
for i in range(n):
    a, b = str(input()).split()
    q = 0
    for i in range(len(a)):
        if ord(a[i]) <= ord(b[i]): q += ord(b[i])-ord(a[i])
        else: q += 26 - ord(a[i]) + ord(b[i])
    print(q)
