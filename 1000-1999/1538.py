alien="ABCD"
while True:
    n=int(input())
    if n==0:break
    tmp=n*n
    r=""
    while tmp!=0:
        r=alien[tmp%4]+r
        tmp//=4
    print(r)
