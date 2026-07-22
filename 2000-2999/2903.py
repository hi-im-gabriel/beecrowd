def mdc(a, b):
    while b:
        a,b =b,a%b
    return a

def faz(a,b):
    if b!=0:
        return (mdc(b,a%b))
    else:
        return a

a,b=input().split('.')
a=int(a)
b=int(b)

x=(100*a)+b
result=36000/(mdc(36000,x))
print("%i" % result)
