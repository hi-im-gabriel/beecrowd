while True:
    try:
        n = int(input())
    except EOFError:
        break

    arrivals = [[] for _ in range(1001)]
    for _ in range(n):
        t, c = map(int, input().split())
        arrivals[t].append(c)

    active_times = [[] for _ in range(1001)]
    positions = [0] * 1001
    counts = [0] * 1001
    arrival_sums = [0] * 1001

    current_time = 1
    next_time = 1
    completed = 0
    total_waiting = 0
    active_mask = 0

    while completed < n and current_time < 1000:
        while next_time <= current_time and next_time <= 1000:
            for duration in arrivals[next_time]:
                active_times[duration].append(next_time)
                counts[duration] += 1
                arrival_sums[duration] += next_time
                active_mask |= 1 << duration
            next_time += 1

        if active_mask == 0:
            while next_time <= 1000 and not arrivals[next_time]:
                next_time += 1
            if next_time > 1000:
                break
            current_time = next_time
            continue

        lowest_bit = active_mask & -active_mask
        duration = lowest_bit.bit_length() - 1
        request_time = active_times[duration][positions[duration]]
        positions[duration] += 1
        counts[duration] -= 1
        arrival_sums[duration] -= request_time

        if counts[duration] == 0:
            active_mask ^= lowest_bit

        total_waiting += current_time - request_time
        current_time += duration
        completed += 1

    if completed < n:
        while next_time <= 1000:
            for duration in arrivals[next_time]:
                counts[duration] += 1
                arrival_sums[duration] += next_time
            next_time += 1

        for duration in range(1, 1001):
            amount = counts[duration]
            if amount:
                total_waiting += amount * current_time
                total_waiting += duration * amount * (amount - 1) // 2
                total_waiting -= arrival_sums[duration]
                current_time += duration * amount

    print(total_waiting)
