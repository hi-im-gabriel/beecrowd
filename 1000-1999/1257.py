alfa={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
for n in range(int(input())):
    linhas=int(input())
    result=aux=0
    for i in range(linhas):
        string=input()
        for j in string:
            result+=alfa[j]+i+aux
            aux+=1
        aux=0
    print(result)
