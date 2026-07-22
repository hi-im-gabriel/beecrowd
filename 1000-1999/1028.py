def res(f1, f2):
    return f1 if not f2 else res(f2,f1%f2)
for _ in range(int(input())):
    f1,f2=map(int,input().split())
    print(res(f1,f2))
