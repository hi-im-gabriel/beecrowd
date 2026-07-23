def res(x):
    if x[0]==x[1]==x[2]==x[3]:return -1
    c=0
    while x != '6174':
        maior,menor=int(''.join(sorted(x, reverse=True))),int(''.join(sorted(x)))
        x=str(maior-menor)
        while len(x)<4:x='0'+x
        c+=1
    return c

n=int(input())
for i in range(n):
    x=input()
    while len(x) < 4:x='0'+x
    x=res(x)
    print(f"Caso #{i+1}: {x}")
