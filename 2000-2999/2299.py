import sys

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

teste = 1
out = []

while True:
    c = next(it)
    f = next(it)

    if c == 0 and f == 0:
        break

    frases = []
    total_desculpas = 0

    for _ in range(f):
        n = next(it)
        d = next(it)

        frases.append((n, d))
        total_desculpas += d

    bloco = total_desculpas + 1
    estados = 1

    limite = (c + 1) * bloco
    mascara = (1 << limite) - 1

    for n, d in frases:
        deslocamento = n * bloco + d
        estados |= estados << deslocamento
        estados &= mascara

    valores = estados
    deslocamento = bloco

    while deslocamento < limite:
        valores |= valores >> deslocamento
        deslocamento *= 2

    valores &= (1 << bloco) - 1

    resposta = valores.bit_length() - 1

    out.append(f"Teste {teste}")
    out.append(str(resposta))
    out.append("")

    teste += 1

sys.stdout.write("\n".join(out) + "\n")

