while True:
    try:
        direito = [ ]
        esquerdo = [ ]
        pares = 0
        for x in range(int(input())):
            valores = input()
            partes = valores.split()
            M = int(partes[0])
            L = str(partes[1])
            if L == "D":
                direito.append(M)
            if L == "E":
                esquerdo.append(M)
        for x in direito:
            if x in esquerdo:
                pares += 1
                esquerdo.remove(x)
        print(pares)
    except:break
