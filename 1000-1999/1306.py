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
#n= list(map(int,input().split()))
caso=0
while True:
    caso+=1
    r,n=input().split()
    r=int(r)
    n=int(n)
    aux=0
    if r==0 and n==0:
        break
    if n>=r:
        print("Case %d: 0" % (caso))
    else:
        j=1
        while(j<27):
            if(n*(j+1) >= r):
                print("Case %d: %d" % (caso,j))
                aux=1
                break
            j+=1
        if aux==0:
            print("Case %d: impossible" % (caso))
