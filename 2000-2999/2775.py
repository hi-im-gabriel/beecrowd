while True:
    try:
        n = int(input())
    except EOFError:
        break

    packages = list(map(int, input().split()))
    times = list(map(int, input().split()))

    total_time = 0

    for i in range(n):
        for j in range(i + 1, n):
            if packages[i] > packages[j]:
                total_time += times[i] + times[j]

    print(total_time)
