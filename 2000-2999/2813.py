casaMenos, casaMais, trabalhoMenos, trabalhoMais = 0, 0, 0, 0
for i in range(int(input())):
    trabalho, casa = input().split()
    if trabalho == "chuva" and casaMenos == 0:
        casaMais += 1
        trabalhoMenos += 1
    elif trabalho == "chuva" and casaMenos > 0:
        trabalhoMenos += 1
        casaMenos -= 1
    if casa == "chuva" and trabalhoMenos == 0:
        trabalhoMais += 1
        casaMenos += 1
    elif casa == "chuva" and trabalhoMenos > 0:
        casaMenos += 1
        trabalhoMenos -= 1
print(casaMais, trabalhoMais)
