n = int(input())
codes = input().split()

print("".join(chr(int(code, 16)) for code in codes[:n]))
