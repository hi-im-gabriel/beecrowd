#n= list(map(int,input().split()))
#string.split('+',2)
#import re re.sub("[^0-9]",""", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")

while True:
    try:
        s=input()
        s=s.replace('=',' ')
        s=s.replace('+',' ')
        s=s.split()
        tot=0
        if s[0] == 'R':
            tot=int(s[2])-int(s[1])
        elif s[1] == 'L':
            tot=int(s[2])-int(s[0])
        else:
            tot=int(s[0])+int(s[1])
        print(tot)


    except EOFError:
        break
