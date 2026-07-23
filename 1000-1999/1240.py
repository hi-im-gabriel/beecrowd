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
#n= list(map(int,input().split()))
x=int(input())
for i in range(x):
    n1,n2=input().split()
    if n2==n1[len(n1)-len(n2):len(n1)]:
        print("encaixa")
    else:
        print("nao encaixa")
