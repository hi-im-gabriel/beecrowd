#n= list(map(int,input().split()))
#string.split('+',2)
#import re re.sub("[^0-9]",""", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")

c = int(input())
for i in range(c):
    saida = ""
    reverse = ""
    a, b = map(int, input().split())
    while a <= b:
        saida += str(a)
        a += 1

    reverse = saida + saida[::-1]
    print(reverse)
