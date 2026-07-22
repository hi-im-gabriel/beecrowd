x=list(map(int,input().split()))
print((24+sum(x))%24) if sum(x)<0 else print(sum(x)%24)
