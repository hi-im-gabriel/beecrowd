aux=med=0
while True:
    idade=int(input())
    if idade<0:break
    aux+=1
    med+=idade
print("%.2f"%(med/aux))
