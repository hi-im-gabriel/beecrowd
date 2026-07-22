tempo, distancia, vel = 0, 0, 1
while True:
    try:
        string = input()                

        if ' ' in string:
            h, m, s = map(int, string.split(' ')[0].split(":"))
            if tempo != 0:
                distancia += (float(((h * 3600 + m * 60 + s) - tempo) * vel) / 3600)
            vel = int(string.split()[-1])
            tempo = h * 3600 + m * 60 + s
        else:
            h, m, s = map(int, string.split(":"))
            distancia += (float(((h * 3600 + m * 60 + s) - tempo) * vel) / 3600)
            print("%02d:%02d:%02d %.2f km" % (h, m, s, distancia))
            tempo = h * 3600 + m * 60 + s
    except EOFError:
        break
