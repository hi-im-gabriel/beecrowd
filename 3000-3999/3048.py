lista = []

for _ in range(int(input())):
    number = input()
    if not lista:
        lista.append(number)
    elif number != lista[-1]:
        lista.append(number)

print(len(lista))
