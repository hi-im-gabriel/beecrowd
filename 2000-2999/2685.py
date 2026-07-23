1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
while True:
    try:
        x = input()
        x = int(x)
        if(x>=0 and x<90):
            print("Bom Dia!!")
        elif(x>=90 and x<180):
            print("Boa Tarde!!")
        elif(x>=180 and x<270):
            print("Boa Noite!!")
        elif(x>=270 and x<360):
            print("De Madrugada!!")
        elif(x==360):
            print("Bom Dia!!")
    except EOFError:
        break
