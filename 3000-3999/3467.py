while True:
    try:
        s = input()
        if s[2] == 'L':
            print('Esse eh o meu lugar')
        else:
            print('Oi, Leonard')
    except EOFError:
        break
