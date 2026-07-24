pares = {')': '(', ']': '[', '}': '{'}

T = int(input())

for _ in range(T):
    cadeia = input().strip()
    pilha = []
    valida = True

    for caractere in cadeia:
        if caractere in '([{':
            pilha.append(caractere)
        elif not pilha or pilha.pop() != pares[caractere]:
            valida = False
            break

    print('S' if valida and not pilha else 'N')
