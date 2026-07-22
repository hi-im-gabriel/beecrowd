d=dict()
for _ in range(int(input())):
    s=input().split(' ',1)
    d[s[0]]=list(map(int,s[1].split()))
d=dict(sorted(d.items(), key=lambda x: x[0]))
d=dict(sorted(d.items(), key=lambda x: x[1][2],reverse=True))
d=dict(sorted(d.items(), key=lambda x: x[1][1],reverse=True))
d=dict(sorted(d.items(), key=lambda x: x[1][0],reverse=True))
for i,j in d.items():print(i,*j,sep=" ")
