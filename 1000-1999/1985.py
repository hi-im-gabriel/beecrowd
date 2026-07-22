d={1001: 1.50, 1002: 2.50, 1003: 3.50, 1004: 4.50, 1005:5.50}
soma=0.00
for p in range(int(input())):
    a,b=map(int,input().split())
    soma+=(d.get(a)*b)
print("%.2f"%soma)
