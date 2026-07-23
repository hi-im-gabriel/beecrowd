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
26
#n,m=map(int, input().split())
#n= list(map(int,input().split()))
#string.split("+",2)
#string.append(input()) stringarray
#string = string.replace(a, "")
#import re re.sub("[^0-9]", ", string)
#print(menor, end=" ")
while True:
    try:
        n,m=input().split()
        n=int(n)
        m=int(m)
        aux=0
        while n:
            i,x=input().split()
            i=int(i)
            x=int(x)
            if i==m and x==0:
                aux+=1
            n-=1
        print(aux)
    except EOFError:
        break
