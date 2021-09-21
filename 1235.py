for i in range(int(input())):
    s=input()
    tam=len(s)
    e=[]
    d=[]
    if tam%2!=0:
        i=0
        while i<=(int(tam/2)-1):
            e.append(s[i])
            i+=1
        i=int(tam/2)
        while i<=tam-1:
            d.append(s[i])
            i+=1
    else:
        i=0
        while i<=int(tam/2)-1:
            e.append(s[i])
            i+=1
        i=int(tam/2)
        while i<=int(tam-1):
            d.append(s[i])
            i+=1
    e.reverse()
    d.reverse()
    print(*e,sep="",end="")
    print(*d,sep="")
