a = input().strip()
b = input().strip()

if len(a) < len(b):
    a, b = b, a

lcs = [0] * (len(b) + 1)

for char_a in a:
    previous = 0
    for j, char_b in enumerate(b, 1):
        current = lcs[j]
        if char_a == char_b:
            lcs[j] = previous + 1
        elif lcs[j - 1] > lcs[j]:
            lcs[j] = lcs[j - 1]
        previous = current

print(len(a) + len(b) - lcs[-1])
