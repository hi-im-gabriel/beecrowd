while True:
    s=input().split()
    if len(s)==1 and len(s[0])==1 and s[0]=='*':break
    tam=len(s)
    f=[]
    for i in range(tam):f.append(s[i][0].lower())
    tam=len(f)
    print("Y") if f.count(f[0])==tam else print("N")
