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
#n= list(map(int,input().split()))
#string.split("+",2)
#import re re.sub("[^0-9]", ", string)
#string.append(input()) array
n=int(input())
while n:
    x=int(input())
    string=list(map(int,input().split()))
    ordena=sorted(string,reverse=True)
    tam=len(string)-1
    alunos=0
    i=0
    while i<=tam:
        if string[i]==ordena[i]:
            alunos+=1
        i+=1
    print(alunos)
    n-=1
