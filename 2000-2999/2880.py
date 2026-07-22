def cp(x, y):
    for i in range(len(x)):
        if x[i] == y[i]: return False
    return True
a=str(input())
b=str(input())
q=len(a)-len(b)+1

t=len(b)
c=0
for g in range(q):
    if cp(a[g:t+g],b):c+=1
print(c)
