#n= list(map(int,input().split()))
import math
while True:
    try:
        D,VF,VG=input().split()
        D=float(D)
        VF=float(VF)
        VG=float(VG)

        dist= math.sqrt(144+D*D)
        tf=12/VF
        tg=dist/VG

        if tg <= tf:
            print("S")
        else:
            print("N")



    except EOFError:
        break
