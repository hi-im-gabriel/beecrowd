par=[]
impar=[]
for _ in range(int(input())):
    n=int(input())
    if n%2==0:par.append(n)
    else:impar.append(n)
par.sort()
impar.sort(reverse=True)
print(*(par+impar),sep="\n")
