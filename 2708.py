aux=0
aux2=0
while True:
    string=list(map(str,input().split()))
    if string[0]=="ABEND":break
    elif string[0]=='SALIDA':
        aux+=int(string[1])
        aux2+=1
    else:
        aux-=int(string[1])
        aux2-=1
print(aux)
print(aux2)
