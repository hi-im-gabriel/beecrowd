from operator import mul

G, A, M, C = map(int, input().split())


def read_row():
    row = input().split()
    while not row:
        row = input().split()
    return tuple(map(int, row))


courses = [read_row() for _ in range(G)]
materials = [read_row() for _ in range(A)]
prices_by_campus = list(zip(*(read_row() for _ in range(M))))

activity_costs_by_campus = [
    tuple(sum(map(mul, activity, prices)) for activity in materials)
    for prices in prices_by_campus
]

result = [
    [sum(map(mul, course, activity_costs)) for activity_costs in activity_costs_by_campus]
    for course in courses
]

widths = [max(len(str(row[campus])) for row in result) for campus in range(C)]

for row in result:
    print(" ".join(str(value).rjust(widths[campus]) for campus, value in enumerate(row)))
