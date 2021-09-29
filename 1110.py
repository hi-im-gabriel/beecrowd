while True:
    n=int(input())
    numeros=[]
    string=[]
    if n==0:break
    for i in range(1,n+1):numeros.append(i)  
    while len(numeros) > 1:
        string.append(str(numeros.pop(0)))
        numeros.insert(len(numeros) - 1, numeros.pop(0))
    print("Discarded cards: " + ", ".join(string), end="")
    print("\nRemaining card: " + str(numeros[0]), end="\n")
