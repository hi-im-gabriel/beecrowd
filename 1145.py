x,y=map(int,input().split())
for i in range(1,y+1,x):
    a=[n for n in range(i,i+x) if n<=y]
    print(*a,sep=" ")
