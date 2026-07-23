#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

while True:
    try:
        x = int(input())
    except:
        break

    ts=0
    s = []
    q = []
    pq = []

    stack=1
    queue=1
    prioriq=1

    for _ in range(x):
        opc, n = input().split()

        if int(opc) == 1:
            s.append(int(n))
            ts+=1

            q.append(int(n))

            pq.append(int(n))
            pq.sort(reverse=True)

        else:
            if s[ts-1] == int(n) and stack == 1:
                ts-=1
                del s[ts]
            else: stack=0

            if q[0] == int(n) and queue == 1: del q[0]
            else: queue=0

            if pq[0] == int(n) and prioriq == 1: del pq[0]
            else: prioriq=0

    if (stack == 1 and queue == 1) or (stack == 1 and prioriq == 1) or (queue == 1 and prioriq == 1): print("not sure")
    elif stack: print("stack")
    elif queue: print("queue")
    elif prioriq: print("priority queue")
    else: print("impossible")
