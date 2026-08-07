quantidade = int(input())
notas = set()

for _ in range(quantidade):
    notas.add((int(input()) - 1) % 12)

intervalos = {0, 2, 4, 5, 7, 9, 11}
nomes = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

for tom in range(12):
    if all((nota - tom) % 12 in intervalos for nota in notas):
        print(nomes[tom])
        break
else:
    print("desafinado")
