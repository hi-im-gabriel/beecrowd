from math import factorial as fat #importa o factorial de math para ser usado como "fat"

while True:
    try:
        x,y=map(int,input().split())
        soma=fat(x)+fat(y)
        print(soma)
    except EOFError:break
