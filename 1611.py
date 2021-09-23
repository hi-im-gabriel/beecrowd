def elevadorLotado(paradas, capacidade):
   energiaGasta = 0
   while paradas:
      ultimo = paradas[-1]
      energiaGasta += 2*ultimo
      paradas = paradas[:-capacidade]
   return energiaGasta
testes = int(input())
for x in range(testes):
   NCM = input().split()
   capacidade = int(NCM[1])
   destinhos = list(map(int,input().split()))
   destinhos.sort()
   s = elevadorLotado(destinhos, capacidade)
   print(s)
