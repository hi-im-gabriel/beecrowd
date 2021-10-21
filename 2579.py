a,b,c,d=map(int,input().split())
c+=1
d+=1
r=c-1
r*=b
r+=d
print('Direita') if r&1 else print('Esquerda')
