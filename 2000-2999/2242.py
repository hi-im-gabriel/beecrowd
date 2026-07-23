s = input()
vog = ""
for l in s:
    if(l=="a" or l=="e" or l=="i" or l=="o" or l=="u"):
        vog+=l
if(vog == vog[::-1]):
    print("S")
else:
    print("N")
