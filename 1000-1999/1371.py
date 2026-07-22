while True:
    n=int(input())
    if n==0:break
    aux=[]
    i=1
    while i**2 <= n:
        aux.append(i**2)
        i+=1
    for i in range(len(aux)):
        print("%d " %aux[i], end='') if i<len(aux)-1 else print("%d" %aux[i])
