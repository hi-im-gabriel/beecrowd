while True:
    n = int(input())

    if n == 0:
        break

    pontos = {}

    for _ in range(n):
        time, pontuacao = input().split()
        pontos[time] = int(pontuacao)

    for _ in range(n // 2):
        time_a, placar, time_b = input().split()
        gols_a, gols_b = map(int, placar.split("-"))

        pontos[time_a] += gols_a * 3
        pontos[time_b] += gols_b * 3

        if gols_a > gols_b:
            pontos[time_a] += 5
        elif gols_b > gols_a:
            pontos[time_b] += 5
        else:
            pontos[time_a] += 1
            pontos[time_b] += 1

    campeao = max(pontos, key=pontos.get)

    if campeao == "Sport":
        print(f"O Sport foi o campeao com {pontos[campeao]} pontos :D")
    else:
        print(f"O Sport nao foi o campeao. O time campeao foi o {campeao} com {pontos[campeao]} pontos :(")

    print()
