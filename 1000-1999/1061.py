comec=input().split()
hCOMEC=input().split()
final=input().split()
hFINAL=input().split()
di,df=int(comec[1]),int(final[1])
hi,mi,si=int(hCOMEC[0]), int(hCOMEC[2]), int(hCOMEC[4])
hf,mf,sf=int(hFINAL[0]), int(hFINAL[2]), int(hFINAL[4])
mSEG=60
hSEG=mSEG*60
dSEG=hSEG*24
i,f=si+mi*mSEG+hi*hSEG+di*dSEG,sf+mf*mSEG+hf*hSEG+df*dSEG
if i < f:
    tempo=f-i
    dias=int(tempo/dSEG)
    tempo=tempo%dSEG
    horas=int(tempo/hSEG)
    tempo=tempo%hSEG
    minutos=int(tempo/mSEG)
    tempo=tempo%mSEG
    segundos=tempo
    print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")
