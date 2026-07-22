d,x=dict(),0
while True:
    try:
        s=input().replace('+',':=').split(' := ')
        if len(s)==2:d[s[0]]=int(s[1]);x=int(s[1])
        else:
            try:soma1=d[s[1]]
            except:soma1=int(s[1])
            try:soma2=d[s[2]]
            except:soma2=int(s[2])
            d[s[0]],x=soma1+soma2,soma1+soma2
    except EOFError:print(x);break
