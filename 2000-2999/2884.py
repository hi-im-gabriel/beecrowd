n, m = map(int, input().split())
initial = list(map(int, input().split()))
acesas = set(initial[1:])

interruptores = []
for _ in range(n):
    dados = list(map(int, input().split()))
    interruptores.append(dados[1:])

for acionamentos in range(1, 2 * n + 1):
    for lampada in interruptores[(acionamentos - 1) % n]:
        if lampada in acesas:
            acesas.remove(lampada)
        else:
            acesas.add(lampada)

    if not acesas:
        print(acionamentos)
        break
else:
    print(-1)
