def integers():
    while True:
        try:
            for value in input().split():
                yield int(value)
        except EOFError:
            return


values = integers()

while True:
    try:
        m = next(values)
        k = next(values)
    except StopIteration:
        break

    durations = [next(values) for _ in range(m)]
    heard = set()
    elapsed = 0
    answer = -1

    for _ in range(k):
        track = next(values)
        if answer == -1:
            elapsed += durations[track - 1]
            heard.add(track)
            if len(heard) == m:
                answer = elapsed

    print(answer)
