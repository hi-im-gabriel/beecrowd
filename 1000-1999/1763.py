#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
pais=['brasil','alemanha','austria','coreia','espanha','grecia','estados-unidos','inglaterra','australia','portugal','suecia','turquia','argentina','chile','mexico','antardida','canada','irlanda','belgica','italia','libia','siria','marrocos','japao']
frase=['Feliz Natal!','Frohliche Weihnachten!','Frohe Weihnacht!','Chuk Sung Tan!','Feliz Navidad!','Kala Christougena!','Merry Christmas!','Merry Christmas!','Merry Christmas!','Feliz Natal!','God Jul!','Mutlu Noeller','Feliz Navidad!','Feliz Navidad!','Feliz Navidad!','Merry Christmas!','Merry Christmas!','Nollaig Shona Dhuit!','Zalig Kerstfeest!','Buon Natale!','Buon Natale!','Milad Mubarak!','Milad Mubarak!','Merii Kurisumasu!']
while True:
    try:
        s=input()
        try:
            print(frase[pais.index(s)])
        except:
            print("--- NOT FOUND ---")

    except EOFError:
        break
