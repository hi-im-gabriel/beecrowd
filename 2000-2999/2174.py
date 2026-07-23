#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")
#f=list(dict.fromkeys(f)) remover repetidos
n=int(input())
f=[]

while n:
    s=input()
    f.append(s)

    n-=1
f=set(f)
tam=151-int(len(f))
print("Falta(m) %d pomekon(s)." % (tam))
