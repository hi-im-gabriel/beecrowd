t = int(input())

for _ in range(t):
    number = input().strip()
    while not number:
        number = input().strip()

    digits = sorted(number)

    first_nonzero = 0
    while first_nonzero < len(digits) and digits[first_nonzero] == "0":
        first_nonzero += 1

    if first_nonzero == len(digits):
        print("0")
    else:
        digits[0], digits[first_nonzero] = digits[first_nonzero], digits[0]
        print("".join(digits))
