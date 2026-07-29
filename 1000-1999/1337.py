while True:
    try:
        cards = list(map(int, input().split()))
    except EOFError:
        break

    if cards == [0, 0, 0]:
        break

    cards.sort()
    a, b, c = cards

    if a == c:
        if a == 13:
            print('*')
        else:
            print(a + 1, a + 1, a + 1)
    elif a == b or b == c:
        if a == b:
            pair = a
            other = c
        else:
            pair = b
            other = a

        other += 1
        if other == pair:
            other += 1

        if other <= 13:
            result = sorted([pair, pair, other])
            print(*result)
        elif pair < 13:
            pair += 1
            other = 1
            if other == pair:
                other += 1
            result = sorted([pair, pair, other])
            print(*result)
        else:
            print(1, 1, 1)
    else:
        print(1, 1, 2)
