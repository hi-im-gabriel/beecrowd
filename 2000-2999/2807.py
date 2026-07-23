#n,m=map(int, input().split())
#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input()) stringarray
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)
#print(menor, end=' ')

fib = [1, 1]
for x in range(2, 41):
    fib.append(fib[x-1]+fib[x-2])
fib.sort(reverse=True)
n = int(input())
palavra = ''
for x in fib[41-n:]:
    palavra += str(x) + ' '

palavra = palavra[:-1]
print(palavra)
