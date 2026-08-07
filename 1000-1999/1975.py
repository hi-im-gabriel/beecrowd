while True:
    try:
        P, A, R = map(int, input().split())
    except EOFError:
        break

    if P == 0 and A == 0 and R == 0:
        break

    pearls = {input() for _ in range(P)}
    maximum = -1
    winners = set()

    for _ in range(A):
        name = input()
        count = 0

        for _ in range(R):
            if input() in pearls:
                count += 1

        if count > maximum:
            maximum = count
            winners = {name}
        elif count == maximum:
            winners.add(name)

    print(", ".join(sorted(winners)))
