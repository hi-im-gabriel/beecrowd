#n= list(map(int,input().split()))
#string.split("+",2)
#import re re.sub("[^0-9]", ", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")

while True:
    n=int(input())
    planeta=[]
    result=[]
    if n==0:
        break
    while n:
        p,a,x=input().split()
        planeta.append(p)
        result.append(int(a)-int(x))
        n-=1
    menor=min(result)
    print(planeta[result.index(menor)])
