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
space=0
while True:
    try:
        x=int(input())
        b=0
        orde=1
        if space:
            print("")
        space = 1
        if x%4==0 and x%100!=0 or x%400==0:
            print("This is leap year.")
            b=1
            orde=0
        if x%15==0:
            print("This is huluculu festival year.")
            orde=0
        if x%55==0 and b:
            print("This is bulukulu festival year.")
        if orde:
            print("This is an ordinary year.")
    except EOFError:
        break
