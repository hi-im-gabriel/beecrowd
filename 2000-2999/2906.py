f=[]
qtd=0
for _ in range(int(input())):
   s=input().split('@')
   email=s[0].replace('.','')
   if '+' in email:
      aux=email.index('+')
      email=email[0:aux]
   provedor=s[1]
   email=email+"@"+provedor
   if email not in f:
      f.append(email)
      qtd+=1
print(qtd)
