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
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
temp = [0] * 100000
def merge(A, esq, meio, dir):
    trocas = 0
    i, j, k = esq, meio, esq 
    while (i < meio and j <= dir):     
        if (A[i] <= A[j]):
            temp[k] = A[i]
            k, i = k + 1, i + 1
        else:
            temp[k] = A[j]
            k, j = k + 1, j + 1
            trocas += meio - i
    while (i < meio):
        temp[k] = A[i]
        k, i = k + 1, i + 1
    while (j <= dir):
        temp[k] = A[j]
        k, j = k + 1, j + 1
    while (esq <= dir):
        A[esq] = temp[esq]
        esq += 1
    return trocas
def merget(A, esq, dir):
    trocas = 0
    if (esq < dir):
        meio = esq + (dir - esq) // 2
        trocas += merget(A, esq, meio)
        trocas += merget(A, meio + 1, dir)
        trocas += merge(A, esq, meio + 1, dir)
    return trocas
for z in range(int(input())):
    m=int(input())
    vagoes=list(map(int,input().split()))
    aux=merget(vagoes,0,m-1)
    print("Optimal train swapping takes %d swaps." % aux)
