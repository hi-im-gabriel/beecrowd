ld, cd, lv, cv = map(int, input().split())

best = max(min(ld, cd), min(lv, cv))

for wd, hd in ((ld, cd), (cd, ld)):
    for wv, hv in ((lv, cv), (cv, lv)):
        best = max(best, min(hd, hv, wd + wv))

print(best * best)
