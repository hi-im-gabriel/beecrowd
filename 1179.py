impar,par=[],[]
for i in range(15):
    n=int(input())
    if n%2==0:par.append(n)
    else:impar.append(n)
    if len(par)==5:
        for i in range(5):print(f"par[{i}] = {par[i]}")
        par=[]
    if len(impar)==5:
        for i in range(5):print(f"impar[{i}] = {impar[i]}")
        impar=[]
tamP=len(par)
tamI=len(impar)
if tamI>0:
    for i in range(tamI):print(f"impar[{i}] = {impar[i]}")
if tamP>0:
    for i in range(tamP):print(f"par[{i}] = {par[i]}")
