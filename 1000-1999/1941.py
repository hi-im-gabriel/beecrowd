s = input()
values = list(map(int, input().split()))
n = len(s)
special = [0] * n

for position in values[1:]:
    special[position - 1] = 1

base = n + 1
dp = [0] * n

for i in range(n - 1, -1, -1):
    diagonal = 0
    dp[i] = special[i] * base + 1

    for j in range(i + 1, n):
        previous = dp[j]
        best = max(dp[j], dp[j - 1])

        if s[i] == s[j]:
            matched = diagonal + (special[i] + special[j]) * base + 2
            best = max(best, matched)

        dp[j] = best
        diagonal = previous

print(dp[n - 1] % base)
