for _ in range(int(input())):
    s=input().split()
    p1=s[0]
    p2=s[1]
    f=""
    aux=0
    while aux<len(p1) and aux<len(p2):
        f+=p1[aux]+p2[aux]
        aux+=1
    if aux<len(p1):f+=p1[aux:]
    if aux<len(p2):f+=p2[aux:]
    print(f)
