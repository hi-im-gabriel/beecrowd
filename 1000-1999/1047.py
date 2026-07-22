st,sm,et,em=map(int,input().split())
rt=et-st
if rt<0:rt=24+(et-st)
rm=em-sm
if rm<0:
    rm=60+(em-sm)
    rt-=1
if et==st and em==sm:print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if rt<0:rt=24+rt
    print(f"O JOGO DUROU {rt} HORA(S) E {rm} MINUTO(S)")
