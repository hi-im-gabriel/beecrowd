instancia = 1

while True:
    try:
        n = int(input())
    except EOFError:
        break

    alunos = []
    for _ in range(n):
        nome, resolvidos = input().split()
        alunos.append((int(resolvidos), nome))

    alunos.sort(key=lambda aluno: (-aluno[0], aluno[1]))

    print(f"Instancia {instancia}")
    print(alunos[-1][1])
    print()

    instancia += 1
