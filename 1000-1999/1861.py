assasins,deads= {},[]
while True:
    try:
        assassin,dead=input().split()
        if assassin in assasins:assasins[assassin]+=1;deads.append(dead)
        else:assasins[assassin]=1;deads.append(dead)
    except EOFError:break
for i in deads:assasins.pop(i,None)
print('HALL OF MURDERERS')
for i, v in sorted(assasins.items()):print(i, v)
