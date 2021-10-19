for _ in range(int(input())):
    a,b=map(int,input().split())
    d=dict()
    for i in range(a):
        s=input()
        s1=input()
        d[s]=s1
    for i in range(b):
        s=input().split()
        for i in range(len(s)):
            try:
                s[i]=d[s[i]]
            except:pass
        print(*s,sep=" ")
    print()
