n = int(input())

for _ in range(n):
    top = int(input())
    sides = list(map(int, input().split()))
    bottom = int(input())

    faces = [top] + sides + [bottom]
    classic = (
        sorted(faces) == [1, 2, 3, 4, 5, 6]
        and top + bottom == 7
        and sides[0] + sides[2] == 7
        and sides[1] + sides[3] == 7
    )

    print("SIM" if classic else "NAO")
