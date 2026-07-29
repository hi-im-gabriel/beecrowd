areas = sorted(map(int, input().split()))

if areas[0] * areas[3] == areas[1] * areas[2]:
    print("S")
else:
    print("N")
