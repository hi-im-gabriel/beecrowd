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
#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input()) stringarray
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)
l = []
while True:
    try:
        l.append(input())
       
    except EOFError:
        break
       
l = set(l)
print(len(l))
