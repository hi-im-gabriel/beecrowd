test = 1

while True:
    n = int(input())

    if n == 0:
        break

    possibilities = [set(range(10)) for _ in range(6)]

    for _ in range(n):
        data = input().split()
        digits = data[:10]
        password = data[10:]

        for position, letter in enumerate(password):
            index = ord(letter) - ord("A")
            pair = {int(digits[index * 2]), int(digits[index * 2 + 1])}
            possibilities[position] &= pair

    print(f"Teste {test}")
    print(*(next(iter(values)) for values in possibilities), end=" \n")
    print()
    test += 1
