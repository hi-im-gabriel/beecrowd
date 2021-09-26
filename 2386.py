a = int(input())
x=q=0
for n in range(int(input())):
    num = int(input())
    x = a*num
    if x>= 40000000:q=q+1
print(q)
