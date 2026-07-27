t = int(input())

for case in range(1, t + 1):
    n = int(input())
    grades = list(map(int, input().split()))
    highest = max(grades)
    longest = 0
    current = 0

    for grade in grades:
        if grade == highest:
            current += 1
            longest = max(longest, current)
        else:
            current = 0

    print(f"Caso #{case}: {longest}")
