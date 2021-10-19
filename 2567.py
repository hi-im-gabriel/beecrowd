while True:
    try:
        input()
        a=list(map(int,input().split()))
        aux=0
        while len(a) >= 2:
            maior,menor=max(a),min(a)
            a.remove(maior)
            a.remove(menor)
            aux+=(maior-menor)
        print(aux)
    except EOFError:break
