#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
while True:
    try:
        aux = input()
        i = 0
        b = 0
        f = ''
        for j in range(len(aux)):
            if(aux[j] == '_'):
                if(i == 0):
                    f += '<i>'
                    i = 1
                else:
                    f += '</i>'
                    i = 0
            elif(aux[j] == '*'):
                if(b == 0):
                    f += '<b>'
                    b = 1
                else:
                    f += '</b>'
                    b = 0  
            else:
                f += aux[j]       
        print(f)
    except EOFError:
        break
