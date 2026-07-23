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
#string.append(input()) stringarray
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)
while True:
    try:
        n,mini,maxi=input().split()
        n=int(n)
        mini=int(mini)
        maxi=int(maxi)
        cont=0
        while n:
            x=int(input())
            if x >= mini and x <= maxi:
                cont+=1
            n-=1
        print(cont)
    except EOFError:
        break
