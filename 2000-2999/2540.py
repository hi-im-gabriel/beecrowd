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
27
#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input()) stringarray
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)
while True:
    try:
        sim=0
        nao=0
        n=int(input())
        string=input().split()
        i=0
        while i<=n-1:
            if string[i] == '1':
                sim +=1
            else:
                nao +=1
            i+=1
        if sim >= (n*2)/3:
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break
