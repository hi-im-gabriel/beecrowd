players = list(map(int, input().split()))

kung = players.index(1)
lu = players.index(9)

if kung // 2 == lu // 2:
    print("oitavas")
elif kung // 4 == lu // 4:
    print("quartas")
elif kung // 8 == lu // 8:
    print("semifinal")
else:
    print("final")
