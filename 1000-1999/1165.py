def primo(n):
    if n==2:return True
    if n<2:return False
    if n%2==0:return False
    k=3
    while k*k<=n:
        if n%k==0:return False
        k+=2
    return True
for _ in range(int(input())):
    n=int(input())
    print(f"{n} eh primo") if primo(n) else print(f"{n} nao eh primo")
