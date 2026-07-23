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
n=int(input())
while n:
    string=input()
    if int(string[0]) == int(string[2]):
        print(int(string[0])*int(string[2]))
    else:
        if string[1] >= 'A' and string[1] <= 'Z':
            print(int(string[2])-int(string[0]))
        else:
            print(int(string[0])+int(string[2]))
    n-=1
