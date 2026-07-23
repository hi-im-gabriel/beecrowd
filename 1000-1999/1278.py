#n= list(map(int,input().split()))
#string.split('+',2)
#import re re.sub("[^0-9]",""", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")

aux = 0
while True:
    n = int(input())
    if n == 0:
        break
    if aux == 1:
        print()
    l = []
    for i in range(n):
        l.append(' '.join(input().split()))
    m = max(len(i) for i in l)

    for i in range(len(l)):
        for j in range(m-len(l[i])):
            print('', end=' ')
        print(l[i])

    aux = 1
