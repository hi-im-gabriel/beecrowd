#n,m=map(int, input().split())
#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input()) stringarray
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)
#print(menor, end=' ')

while True:
    try:
        n=int(input())
        aux=0
        aux2=0

        while n:
            nota,carga=input().split()
            nota=int(nota)
            carga=int(carga)
            aux+=(nota*carga)
            aux2+=carga

            n-=1
        print("%.4lf" % (aux/(aux2*100.0)))

    except EOFError:
        break
