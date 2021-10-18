from math import tan
while True:
    try:
        a,d,r=map(float,input().split())
        print("%.4lf"%(a+tan((r-90.00)*(3.14159265358979323846/180.00))*d))
    except:break
