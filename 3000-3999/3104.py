a = input().strip()
b = int(input())

remainder = 0

for digit in a:
    remainder = (remainder * 10 + int(digit)) % b

print(remainder)
