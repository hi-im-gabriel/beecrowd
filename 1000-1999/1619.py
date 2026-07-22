from datetime import date
for _ in range(int(input())):
    a1,a2=input().split()
    a1,m1,d1=[int(x)for x in a1.split('-')]
    a2,m2,d2=[int(x)for x in a2.split('-')]
    a1=date(a1,m1,d1)
    a2=date(a2,m2,d2)
    print(abs(a1-a2).days)
