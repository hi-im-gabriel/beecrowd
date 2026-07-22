for i in range(int(input())):
    x=int(input())
    sum=0
    for i in range(1,x):
        if x%i==0:sum+=i
    print(f"{x} eh perfeito") if x==sum else print(f"{x} nao eh perfeito")
