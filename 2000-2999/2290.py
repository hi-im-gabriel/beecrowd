def read_tokens():
    while True:
        try:
            for token in input().split():
                yield int(token)
        except EOFError:
            return


tokens = iter(read_tokens())

while True:
    try:
        n = next(tokens)
    except StopIteration:
        break

    if n == 0:
        break

    alone = set()

    for _ in range(n):
        number = next(tokens)

        if number in alone:
            alone.remove(number)
        else:
            alone.add(number)

    print(*sorted(alone))
