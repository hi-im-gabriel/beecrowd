from collections import deque

Oeste = deque()
Sul = deque()
Norte = deque()
Leste = deque()

Total = deque()

def adc(PC):
    global Oeste, Sul, Norte, Leste, Total

    while True:
        Pouso = input()

        if Pouso == "0":
            break
        elif Pouso == "-1":
            PC = Oeste
        elif Pouso == "-2":
            PC = Sul
        elif Pouso == "-3":
            PC = Norte
        elif Pouso == "-4":
            PC = Leste
        else:
            PC.append(Pouso)

    tamanho = len(Oeste) + len(Sul) + len(Norte) + len(Leste)
    for _ in range(tamanho):
        if Oeste:
            Total.append(Oeste.popleft())
        if Norte:
            Total.append(Norte.popleft())
        if Sul:
            Total.append(Sul.popleft())
        if Leste:
            Total.append(Leste.popleft())

    f = " " + " ".join(Total) + " "
    print(f.strip())

PC = int(input())

if PC == -1:
    adc(Oeste)
elif PC == -2:
    adc(Sul)
elif PC == -3:
    adc(Norte)
elif PC == -4:
    adc(Leste)
