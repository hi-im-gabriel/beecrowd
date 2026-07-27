T, M, N = map(int, input().split())
MOD = 10**9 + 7
levels = N - M + 1
programs = [1] * levels

for _ in range(T - 1):
    programs = [programs[1]] + [
        (programs[i - 1] + programs[i + 1]) % MOD
        for i in range(1, levels - 1)
    ] + [programs[-2]]

print(sum(programs) % MOD)
