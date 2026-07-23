#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
#d=dict()
#d[key]=s[value]
#d=dict(sorted(d.items(), key=lambda item: item[1]))
while True:
   try:
      epr=ehd=intr=0
      for i in range(int(input())):
         s=input().split()
         if s[1]=="EPR":epr+=1
         elif s[1]=="EHD":ehd+=1
         else:intr+=1
      print(f"EPR: {epr}\nEHD: {ehd}\nINTRUSOS: {intr}")
   except EOFError:break
