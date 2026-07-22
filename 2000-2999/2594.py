for _ in range(int(input())):
    s = input()
    f = input()
    res = []
    aux = ''
    if s == f:res.append(0)
    elif s.startswith(f + ' '):res.append(0)
    fspace,i=' '+f+' ',0
    while i!=-1:
        i=s.find(fspace,i+1)
        if i!=-1:res.append(i + 1)
    if s.endswith(' ' + f):res.append(len(s)-(len(f)))
    for i in res:aux+=str(i)+' '
    print(aux[:-1]) if len(res)>0 else print(-1)
