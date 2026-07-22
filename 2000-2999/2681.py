def res(numero):
    aux=0
    for i in range(len(numero)):aux=(((aux*10)+int(numero[i]))%86400)
    return aux
def res2(a,b):
    if (b==0):return 1
    res=1
    while (b>1):
        if (b%2==1):res=((res*(a%86400))%86400)
        a*=a%86400
        a%=86400
        b>>=1
    return (((a%86400)*(res%86400))%86400)
numero=str(input())
n=res(numero)
tot=(res2(2,n)-1)
h=tot//3600
tot=(tot%3600)
m,s=tot//60,tot%60
print(f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}")
