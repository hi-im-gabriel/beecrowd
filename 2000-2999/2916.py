MOD = 1000000007


def values():
    while True:
        try:
            for value in input().split():
                yield int(value)
        except EOFError:
            return


data = values()

while True:
    try:
        n = next(data)
        k = next(data)
    except StopIteration:
        break

    grades = []

    for _ in range(n):
        grades.append(next(data))

    grades.sort(reverse=True)

    print(sum(grades[:k]) % MOD)
