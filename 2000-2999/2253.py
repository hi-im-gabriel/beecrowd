while True:
    try:
        s=input()
        tam=len(s)
        minuscula=0
        maiuscula=0
        numero=0
        pontuacao=0
        if(tam<6 or tam>32):
            print("Senha invalida.")
        else:
            i=0
            while i<=tam-1:
                if s[i]>='a' and s[i]<='z':
                    minuscula+=1
                elif s[i]>='A' and s[i]<='Z':
                    maiuscula+=1
                elif s[i].isdecimal()==True:
                    numero+=1
                else:
                    pontuacao+=1
                    break
                i+=1

            if pontuacao>0:
                print("Senha invalida.")
            else:
                if minuscula>0 and maiuscula>0 and numero>0:
                    print("Senha valida.")
                else:
                    print("Senha invalida.")
    except EOFError:
        break
