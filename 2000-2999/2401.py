factors = {
    1: (0, 0, 0, 0),
    2: (1, 0, 0, 0),
    3: (0, 1, 0, 0),
    4: (2, 0, 0, 0),
    5: (0, 0, 1, 0),
    6: (1, 1, 0, 0),
    7: (0, 0, 0, 1),
    8: (3, 0, 0, 0),
    9: (0, 2, 0, 0),
}

exponents = [0, 0, 0, 0]

for _ in range(int(input())):
    number, operation = input().split()
    direction = 1 if operation == "*" else -1

    for index, exponent in enumerate(factors[int(number)]):
        exponents[index] += direction * exponent

result = 1

for prime, exponent in zip((2, 3, 5, 7), exponents):
    result *= prime ** exponent

print(result)
