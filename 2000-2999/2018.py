from collections import defaultdict

medals = defaultdict(lambda: [0, 0, 0])

while True:
    try:
        input()
        gold = input()
        silver = input()
        bronze = input()

        medals[gold][0] += 1
        medals[silver][1] += 1
        medals[bronze][2] += 1
    except EOFError:
        print("Quadro de Medalhas")

        order = sorted(
            medals.items(),
            key=lambda x: (-x[1][0], -x[1][1], -x[1][2], x[0])
        )

        for country, (g, s, b) in order:
            print(f"{country} {g} {s} {b}")
        break
