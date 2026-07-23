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
#n= list(map(int,input().split()))
#string.split('+',2)
def trocar(atual,mov):
    if mov==1:
        v1,v2='A','B'
    elif mov==2:
        v1,v2='B','C'
    elif mov==3:
        v1,v2 ='A','C'
    if atual==v1:
        return v2
    elif atual==v2:
        return v1
    else:
        return atual
n=int(input())
atual=input()
for i in range(n):
    mov=int(input())
    atual = trocar(atual,mov)
print(atual)
