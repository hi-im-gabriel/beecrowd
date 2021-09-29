x,y,z=map(int,input().split())
if x>y:
    if y>z:
        if y-z<x-y:print(":)")
        else:print(":(")
    else:print(":)")
elif y>x:
    if z>y:
        if z-y<y-x:print(":(")
        else:print(":)")
    else:print(":(")
elif z>y:print(":)")
else:print(":(")
