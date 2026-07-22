for i in range(int(input())):
    n,base=input().split()
    base=str(base)
    aux=0
    print("Case %d:"%(i+1))
    if base=="bin":
        aux=int(n, 2)
        print("%d dec"%aux)
        aux=hex(aux).replace('0x','')
        print("%s hex"%aux)
    elif base=="dec":
        n=int(n)
        aux=hex(n).replace('0x','')
        print("%s hex"%aux)
        aux=bin(n).replace('0b','')
        print("%s bin"%aux)
    elif base=="hex":
        aux=int(n, 16)
        print("%d dec"%aux)
        aux=bin(aux).replace('0b','')
        print("%s bin"%aux)
    print()
