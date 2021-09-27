for n in range(int(input())):
    s=input().split()
    for p in s:
        if 'oulupukk' in p:
            if len(p)==10:s[s.index(p)]='Joulupukki'
            if len(p)==11:s[s.index(p)]='Joulupukki.'
    print(*s,sep=" ")
