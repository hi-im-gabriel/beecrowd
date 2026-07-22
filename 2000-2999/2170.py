proj = 1
while True:
    try:
        x, y = map(float,input().split())
        juros = 100*((y/x)-1)

        print(f"Projeto {proj}:")
        print("Percentual dos juros da aplicacao: %.2f %%" % juros)
        print()

        proj+=1
    except EOFError:break
