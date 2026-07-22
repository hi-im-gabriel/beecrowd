x=[int(input())]
for i in range(1,10):x.append(x[i-1]*2)
for i in range(10):print(f"N[{i}] = {x[i]}")
