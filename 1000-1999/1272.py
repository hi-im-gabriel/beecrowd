#n= list(map(int,input().split()))
#string.split('+',2)
#import re re.sub("[^0-9]",""", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")

n=int(input())

while n:
    nome=[]
    string=input().split()
    tam=len(string)-1
    i=0
    while i<=tam:
        nome.append(string[i][0])


        i+=1
    print(*nome,sep="")

    n-=1
