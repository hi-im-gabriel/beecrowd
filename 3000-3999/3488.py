def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

n = int(input())
print(str(isPowerOfTwo(n)).lower())
