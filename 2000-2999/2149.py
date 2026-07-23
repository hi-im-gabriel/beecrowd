#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

fib = [0,1,1,1,2,2]
for i in range(6, 20):
    if(((i-1) % 2) == 0):fib.append(fib[i-1]*fib[i-2])
    else:fib.append(fib[i-1]+fib[i-2])

while True:
    try:
        n = int(input())
        print(fib[n-1])     
    except EOFError:
        break
