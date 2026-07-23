#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

def res(a,b,c):
    if int(a)+int(b)==int(c):return True
    return False
while True:
    s=input().replace('+',' ').replace('=',' ')
    s=s.split()
    print(res(s[0][::-1],s[1][::-1],s[2][::-1]))
    if int(s[0])==int(s[1])==int(s[2])==0:break
