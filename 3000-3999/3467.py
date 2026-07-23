1
2
3
4
5
6
7
8
9
while True:
    try:
        s = input()
        if s[2] == 'L':
            print('Esse eh o meu lugar')
        else:
            print('Oi, Leonard')
    except EOFError:
        break
