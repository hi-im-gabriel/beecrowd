while True:
    try:
        n=float(input())
        i=1
        aux=1
        while i%n:
            i=((i*10)+1)%n
            aux+=1
        print("%.0f" % (aux))
    except EOFError:break
