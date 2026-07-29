caso = 1

while True:
    try:
        n = int(input())
    except EOFError:
        break

    valores = []
    while len(valores) < 10:
        valores.extend(map(float, input().split()))

    digitos = sorted(range(10), key=lambda digito: (-valores[digito], digito))
    senha = ''.join(map(str, digitos[:n]))

    print(f"Caso {caso}: {senha}")
    caso += 1
