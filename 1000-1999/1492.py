def count_ones(n):
    total = 0
    bit = 1
    quantity = n + 1

    while bit <= n:
        cycle = bit * 2
        total += (quantity // cycle) * bit
        remainder = quantity % cycle
        if remainder > bit:
            total += remainder - bit
        bit *= 2

    return total


while True:
    try:
        a, b = map(int, input().split())
        print(count_ones(b) - count_ones(a - 1))
    except EOFError:
        break
