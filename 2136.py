d=dict()
e=dict()
i=1
while True:
    s=input().split()
    if len(s)==1:
        d=dict(sorted(d.items(),key=lambda item: len(item[0]),reverse=True))
        #d=dict(sorted(d.items(),key=lambda item: item[1]))
        e=dict(sorted(e.items(),key=lambda item: (item[1],item[0])))
        for i,j in e.items():
            print(i)
        print()
        for i,j in d.items():
            aux=i
            break
        print(f"Amigo do Habay:\n{aux}")
        #print(d)
        break
    nome,escolha=s[0],s[1]
    if nome not in e:
        e[nome]=1 if escolha=="YES" else 2
    if escolha=="YES" and nome not in d:
        d[nome]=i
    i+=1
