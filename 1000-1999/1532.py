while True:
    try:
        N, V = map(int, input().split())
    except EOFError:
        break

    if N == 0 and V == 0:
        break

    possible = False

    for speed in range(1, V + 1):
        position = 0

        for current_speed in range(speed, 0, -1):
            for _ in range(current_speed):
                position += current_speed

                if position == N:
                    possible = True
                    break

                if position > N:
                    break

            if possible or position > N:
                break

        if possible:
            break

    print("possivel" if possible else "impossivel")
