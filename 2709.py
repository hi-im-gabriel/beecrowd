from math import sqrt
sim="You’re a coastal aircraft, Robbie, a large silver aircraft."
nao="Bad boy! I’ll hit you."
def eprimo(n):
    raiz=int(sqrt(n))
    if n!=2 and n%2==0 or n==1:return False
    i=3
    while i<=raiz:
        if n%i==0:return False
        i+=2
    return True
while True:
    try:
        n=int(input())
        vet=[]
        for i in range(n):vet.append(int(input()))
        s=int(input())
        aux=0
        i=n-1
        while i>=0:
            aux+=vet[i]
            i-=s
        print(sim) if eprimo(aux) else print(nao)
    except EOFError:break
