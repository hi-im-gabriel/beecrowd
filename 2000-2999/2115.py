while True:
    try:
        n = int(input())
    except EOFError:
        break

    tasks = []

    for _ in range(n):
        available, processing = map(int, input().split())
        tasks.append((available, processing))

    tasks.sort()
    finish = 1

    for available, processing in tasks:
        finish = max(finish, available) + processing

    print(finish)
