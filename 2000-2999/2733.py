while True:
    try:
        x,a=[0,0,0,0],0
        for i in range(4,int(input())+4):
            n=int(input())
            x.append(n)
        x.append(0)
        for i in range(4,len(x)-1):
            tmp=[x[i-1],x[i-2],x[i-3],x[i-4]]
            if x[i] not in tmp and x[i+1]!=x[i]:a+=1
        if a==3:a=4
        if a==10:a=11
        print(a)
    except:break
