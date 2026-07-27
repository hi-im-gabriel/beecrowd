instance = 1

while True:
    n, k = map(int, input().split())

    if n == 0 and k == 0:
        break

    names = input().split()

    for i in range(n):
        limit = min(n, i + k + 1)
        smallest = min(range(i, limit), key=lambda position: names[position])
        name = names.pop(smallest)
        names.insert(i, name)
        k -= smallest - i

    print(f"Instancia {instance}")
    print(*names, end=" \n\n")
    instance += 1
