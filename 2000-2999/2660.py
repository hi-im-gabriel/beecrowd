from math import gcd

n, limit = map(int, input().split())
cycles = map(int, input().split())

common_cycle = 1
for cycle in cycles:
    common_cycle = common_cycle * cycle // gcd(common_cycle, cycle)

multiplier = limit // common_cycle
shared_factor = 1
remaining = common_cycle

while True:
    factor = gcd(remaining, multiplier)
    if factor == 1:
        break
    shared_factor *= factor
    remaining //= factor

print(multiplier * shared_factor)
