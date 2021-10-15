def pot2(n):
    if n==0:return False
    return n and not (n&(n-1))

def get_key(val):
    for key, value in d.items():
         if val == value:
             return key

while True:
    x=int(input())
    if x==0:break
    d={'Uilton':0,'Rita':0,'Ingred':0}
    for i in range(x):
        f=list(map(int,input().split()))
        if pot2(f[0]):
            d['Uilton']+=1
            if max(f)==f[0]:d['Uilton']+=1
        if pot2(f[1]):
            d['Rita']+=1
            if max(f)==f[1]:d['Rita']+=1
        if pot2(f[2]):
            d['Ingred']+=1
            if max(f)==f[2]:d['Ingred']+=1
    d=dict(sorted(d.items(),key=lambda x: x[1],reverse=True))
    i=list(d.values())
    print('URI') if i[0]==i[1] else print(get_key(i[0]))
