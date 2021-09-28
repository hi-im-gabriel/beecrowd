aux=[1, 1]
f=[0, 1]
for i in range(2, 41):
    aux.append(aux[i-1]+aux[i-2]+1)
    f.append(f[i-1]+f[i-2])
for t in range(int(input())):
    n=int(input())
    print("fib(%d) = %d calls = %d" %(n, aux[n]-1, f[n]))
