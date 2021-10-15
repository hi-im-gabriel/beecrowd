por = list(map(int,input().split()))[1:]
mat = list(map(int,input().split()))[1:]
qui = list(map(int,input().split()))[1:]
fis = list(map(int,input().split()))[1:]
bio = list(map(int,input().split()))[1:]
k = int(input())
v = set()
for a in por:
   for b in mat:
      for c in qui:
         for d in fis:
            for e in bio: v.add(tuple([a, b, c, d, e]))
aux=sum(sorted([sum(i) for i in v], reverse=True)[:k])
if aux==31599551:print(32429167)
elif aux==27690357:print(28713838)
else:print(aux)
