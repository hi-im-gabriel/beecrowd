#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

def denis(c1=0,c2=0,c3=0):
    return coe[0]*c1 + coe[1]*c2 + coe[2]*c3

def T3():
    for i in alunos:
        for j in alunos:
            for k in alunos:
                if (denis(i,j,k) in lista):
                    return False
                else:
                    lista.append(denis(i,j,k))
    return True

def T2():
    for i in alunos:
        for j in alunos:
            if (denis(i,j) in lista):
                return False
            else:
                lista.append(denis(i,j))
    return True


def T1():
    for i in alunos:
        if(denis(i) in lista):
            return False
        else:
            lista.append(denis(i))
    return True


while True:  
    try:
        entrada = input().split()
        torneios = int(entrada[0])
        coes = input().split()
        alunos = range(1, int(entrada[1]))
        lista = []
        coe = [0] * 3
        for i in range(torneios):
            coe[i] = int(coes[i])

        if (torneios == 1):
            check = T1()
        elif (torneios == 2):
            check = T2()
        else:
            check = T3()

        if (check):
            print('Lucky Denis!')
        else:
            print('Try again later, Denis...')
    except EOFError:
        break
