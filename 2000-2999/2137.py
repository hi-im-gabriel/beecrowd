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
#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input())
while True:
    try:
        n=int(input())
        aux=n
        string = []
        while n:
            string.append(input())
            n-=1
        inteira=sorted(string)
        i=0
        while i<=aux-1:
            print(inteira[i])
            i+=1
    except EOFError:
        break
