MOD = 10 ** 9 + 7

while True:
    try:
        word = input()
    except EOFError:
        break

    counts = {}
    for letter in word:
        counts[letter] = counts.get(letter, 0) + 1

    factorial = [1] * (len(word) + 1)
    for i in range(2, len(word) + 1):
        factorial[i] = factorial[i - 1] * i % MOD

    answer = factorial[len(word)]
    for count in counts.values():
        answer = answer * pow(factorial[count], MOD - 2, MOD) % MOD

    print(answer)
