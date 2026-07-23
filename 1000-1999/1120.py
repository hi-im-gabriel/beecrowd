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
while True:
    D,N=input().split()
    if D=='0' and N=='0':
        break
    nova = ""
    tamanho = len(N)-1
    i=0
    while(i<=tamanho):
        if N[i] != D:
            nova = nova + N[i]
            
        i+=1
    try:
        nova = int(nova)
    except:
        nova = 0
    print(nova)
