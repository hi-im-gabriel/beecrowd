#n= list(map(int,input().split()))
#string.split('+',2)
#import re re.sub("[^0-9]",""", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")

n=int(input())
while n:
    e,d=input().split('k')
    string=['k']
    eX=e.count('a')
    dX=d.count('a')
    i=1
    while i<=eX*dX:
        string.append('a')
        i+=1
    print(*string,sep="")

    n-=1
