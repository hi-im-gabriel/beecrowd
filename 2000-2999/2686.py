#n= list(map(int,input().split()))


while True:
    try:
        x=float(input())
        if x < 90 or x == 360:
            print("Bom Dia!!")
        elif x < 180:
            print("Boa Tarde!!")
        elif x < 270:
            print("Boa Noite!!")
        elif x < 360:
            print("De Madrugada!!")
        else:
            print("Bom Dia!!")

        if x >= 270:
            horas = ((x-270.0)*4.0)/60.0
        else:
            horas = ((x*4.0)/60.0)+6.0
        minu=(horas*60.0)%60.0
        segu=(minu*60.0)%60.0

        if segu > 59:
            segu = 0.0
            minu+= 1.0
        print("%02d:%02d:%02d" % (int(horas), int(minu), int(segu)))




    except EOFError:
        break
