n=int(input())
x=list(map(int,input().split()))
pos=soma=tot=0
aux=True
for i,num in enumerate(x):
    tot+=num
    if num%2==0 and aux:
        att = i+1
        soma+=((i*2)+1)-pos
        aux=False
    if num-1==0 and aux:pos=i+1
else:
    if(soma>0):tot-=soma
    else:
        att=n
        tot-=att
print(att,tot)
