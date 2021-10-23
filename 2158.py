c=1
while True:
    try:
        fp,fh=map(int,input().split())
        lig=((5*fp+6*fh)//2)
        ato=2+lig-fp-fh
        print(f'Molecula #{c}.:.\nPossui {ato} atomos e {lig} ligacoes\n')
        c+=1  
    except EOFError:break
