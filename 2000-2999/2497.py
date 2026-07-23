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
#n,m=map(int, input().split())
#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input()) stringarray
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)
#print(menor, end=' ')
i=1
while True:
    try:
        n=int(input())
        if n < 0:
            break
        print("Experiment %d: %d full cycle(s)" % (i,n/2))
        i+=1
        
    except EOFError:
        break
