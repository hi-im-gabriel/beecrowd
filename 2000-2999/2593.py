import string
alfa=string.ascii_lowercase
texto=input()
texto=" "+texto+" "
input()
palavra=input().split()
for c in palavra:
    f=[]
    i=0
    while True:
        s=texto.find(c,i)
        if s==-1:break
        i=s+len(c)
        try:
            if texto[s-1] not in alfa and texto[i] not in alfa:f.append(s-1)
        except:pass
    if not f:f.append(-1)
    print(*f,sep=" ")
