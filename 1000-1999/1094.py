tot=coe=rat=sap=0
for i in range(int(input())):
    n,s=input().split()
    n=int(n)
    tot+=n
    if s=='C':coe+=n
    elif s=='R':rat+=n
    elif s=='S':sap+=n
print(f"Total: {tot} cobaias\nTotal de coelhos: {coe}\nTotal de ratos: {rat}\nTotal de sapos: {sap}")
p=(coe/tot)*100
print("Percentual de coelhos: %.2f"%p,end="")
print(" %")
p=(rat/tot)*100
print("Percentual de ratos: %.2f"%p,end="")
print(" %")
p=(sap/tot)*100
print("Percentual de sapos: %.2f"%p,end="")
print(" %")
