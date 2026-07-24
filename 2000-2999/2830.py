k = int(input())
l = int(input())

fases = ["oitavas", "quartas", "semifinal", "final"]

for fase in fases:
    if (k - 1) // 2 == (l - 1) // 2:
        print(fase)
        break
    k = (k + 1) // 2
    l = (l + 1) // 2
