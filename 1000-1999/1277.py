for i in range(int(input())):
    f=[]
    n=int(input())
    nomes=input().split()
    freq=input().split()

    for j in range(n):
        tam=len(freq[j])
        presente=desc=0
        for k in range(tam):
            if freq[j][k]=='P':
                presente+=1
            elif freq[j][k]=='M':
                desc+=1
        presente=float((presente/(tam-desc))*100)
        if presente < 75.00:
            f.append(nomes[j])
    print(*f,sep=" ")
