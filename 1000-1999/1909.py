def gcd(a, b):return a if b==0 else gcd(b,a%b)
def lcm(a, b):return a*b//gcd(a,b)

def res(t, l):
    bounce_time,aux = 0,1
    balls_time = [False]*(int(1e5)+1)
    for x in l:balls_time[x],aux = True,lcm(aux, x)
    if aux <= t:
        for x in range(2, t+1):
            if not t % x and not balls_time[x] and lcm(aux, x) == t:bounce_time = x;break
        if bounce_time == 0:return 'impossivel'
        return str(bounce_time)
    else:return 'impossivel'
    
while True:
    t = int(input().split()[1])
    if t == 0:break
    l = list(map(int,input().split()))
    print(res(t, l))
