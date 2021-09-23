S  = int(input())
Qi = map(int,input().split())
Ni = map(int,input().split())
Qi = sorted(Qi)
Ni = sorted(Ni)
ganha = 0
for soldado in range(S):
    if Ni[soldado] > Qi[ganha]:ganha+=1
print(ganha)
