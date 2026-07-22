fibolista = [0, 1]
def fib(n):
    if n <= 0:return 0
    elif n <= len(fibolista):return fibolista[n - 1]
    else:
        temp_fib=fib(n-1)+fib(n-2)
        fibolista.append(temp_fib)
        return temp_fib
x=[]
for i in range(61):x.append(fib(i+1))
for _ in range(int(input())):
    n=int(input())
    print(f"Fib({n}) = {x[n]}")
