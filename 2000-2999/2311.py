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
28
x = int(input())
while(x>=1):
    i = 1
    soma = 0
    nome = str(input())
    difi = float(input())
    n1,n2,n3,n4,n5,n6,n7 = input().split()
    n1=float(n1)
    n2=float(n2)
    n3=float(n3)
    n4=float(n4)
    n5=float(n5)
    n6=float(n6)
    n7=float(n7)
    sort = [n1,n2,n3,n4,n5,n6,n7]
    sort = sorted(sort)
    while(i<=5):
        soma = soma + sort[i]
        i = i + 1
    soma = soma*difi
    print("%s %.2f" % (nome,soma))
    x = x - 1
