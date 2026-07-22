for n in range(int(input())):
    a,b=input().split()
    if len(a)<len(b):print("nao encaixa")
    else:
        print("encaixa") if a[len(a)-len(b)::]==b else print("nao encaixa")
