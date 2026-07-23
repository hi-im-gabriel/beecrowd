1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input()) stringarray
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)
n = int(input())
k = int(input())
competidor = [int(input()) for x in range(n)]
competidor.sort(reverse=True)
aux = k
while aux < n and competidor[aux] == competidor[k-1]:
    aux += 1
print(aux)
