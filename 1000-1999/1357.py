braille = {
    '1': ('*.', '..', '..'),
    '2': ('*.', '*.', '..'),
    '3': ('**', '..', '..'),
    '4': ('**', '.*', '..'),
    '5': ('*.', '.*', '..'),
    '6': ('**', '*.', '..'),
    '7': ('**', '**', '..'),
    '8': ('*.', '**', '..'),
    '9': ('.*', '*.', '..'),
    '0': ('.*', '**', '..')
}

reverse_braille = {value: key for key, value in braille.items()}

while True:
    d = int(input())
    if d == 0:
        break

    translation_type = input()

    if translation_type == 'S':
        message = input()
        for row in range(3):
            print(' '.join(braille[digit][row] for digit in message))
    else:
        rows = [input().split() for _ in range(3)]
        result = ''
        for i in range(d):
            cell = (rows[0][i], rows[1][i], rows[2][i])
            result += reverse_braille[cell]
        print(result)
