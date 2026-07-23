#x=list(map(int,input().split()))
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
#d=dict()
#d[key]=s[value]
#d=dict(sorted(d.items(), key=lambda item: item[1]))
dp=v=w=None
def knapsack(N, M):
    if N == 0 or M == 0:
        return 0

    if dp[N][M] == 0:
        if M >= W[N]:
            dp[N][M] = max(V[N] + knapsack(N - 1, M - W[N]), knapsack(N - 1, M))
        else:
            dp[N][M] = knapsack(N - 1, M)

    return dp[N][M]


while True:
    N=int(input())
    if N==0:break
    V=[0]
    W=[0]
    for _ in range(N):
        val, weight = map(int, input().split())
        V.append(val)
        W.append(weight)
    M = int(input())
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    print(knapsack(N, M))
