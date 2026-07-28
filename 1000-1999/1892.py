while True:
    try:
        n = int(input())
    except EOFError:
        break

    students = [input() for _ in range(n)]
    positions = {student: i + 1 for i, student in enumerate(sorted(students))}
    tree = [0] * (n + 1)
    inversions = 0

    for i, student in enumerate(students):
        position = positions[student]
        total = 0
        index = position
        while index > 0:
            total += tree[index]
            index -= index & -index

        inversions += i - total
        index = position
        while index <= n:
            tree[index] += 1
            index += index & -index

    print(inversions)
