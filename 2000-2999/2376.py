t=['AB','CD','EF','GH','IJ','KL','MN','OP']
for i in range(8):
    x=list(map(int,input().split()))
    aux = 0 if max(x)==x[1] else 1
    t[i]=t[i].replace(t[i][aux],'')
for i in range(0,8,2):t[i]+=t[i+1]
t=t[::2]
for i in range(4):
    x=list(map(int,input().split()))
    aux = 0 if max(x)==x[1] else 1
    t[i]=t[i].replace(t[i][aux],'')
for i in range(0,4,2):t[i]+=t[i+1]
t=t[::2]
for i in range(2):
    x=list(map(int,input().split()))
    aux = 0 if max(x)==x[1] else 1
    t[i]=t[i].replace(t[i][aux],'')
x=list(map(int,input().split()))
print(t[0]) if max(x)==x[0] else print(t[1])
