packages = []

while True:
    try:
        data = input().split()
    except EOFError:
        break

    if not data or data[0] == "1":
        continue

    if data[0] == "0":
        packages.sort()

        for package in packages:
            print(f"Package {package:03d}")

        print()
        packages = []
    else:
        packages.append(int(data[-1]))
