from math import sqrt
PI = 3.1415926535897
while True:
    try:
        n= list(map(int,input().split()))
        n.sort()
        p=(n[0]+n[1]+n[2])/2.0
        A=sqrt(p*(p-n[0])*(p-n[1])*(p-n[2]))
        cp=pow(A/p,2)*PI
        cg=pow((n[0]*n[1]*n[2])/(4*A),2)*PI
        v=A-cp
        g=cg-A
        r=cp
        print("%.4f %.4f %.4f" % (g,v,r))
    except EOFError:break
