x=[]
for _ in range(int(input())):x.append(int(input()))
s=list(dict.fromkeys(sorted(x)))
for i in s:print(f"{i} aparece {x.count(i)} vez(es)")
