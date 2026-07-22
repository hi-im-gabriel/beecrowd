while True:
    try:
        q,d,p=map(int,input().split())
        aux=int((d*q*p)/(p-q))
        if aux==1:print("%d pagina" % aux)
        else: print("%d paginas" % aux)
    except:break
