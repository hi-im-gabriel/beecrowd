i=1
while True:
    a=input()
    if int(a)==0:break
    if i!=1:print()
    s=input()
    print(f"Instancia {i}")
    i+=1
    print("verdadeira") if a in s else print("falsa")
