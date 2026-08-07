t = int(input())

for _ in range(t):
    p, n = map(int, input().split())

    for _ in range(n):
        grades = [int(round(float(value) * 10)) for value in input().split()]
        total = sum(grades)

        if total < 40 * p:
            result = total / (10 * p)
        else:
            limit = 100 if total >= 70 * p else 69
            candidates = [grade for grade in grades if grade <= limit and grade * p >= total]

            if candidates:
                result = max(candidates) / 10
            else:
                result = total / (10 * p)

        print(f"{result:.2f}")
