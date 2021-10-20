def printar(h,m):
    h8=h4=h2=m32=m16=m8=m4=m2=0
    h8=h//8
    h%=8
    h4=h//4
    h%=4
    h2=h//2
    h%=2
    m32=m//32
    m%=32
    m16=m//16
    m%=16
    m8=m//8
    m%=8
    m4=m//4
    m%=4
    m2=m//2
    m%=2
    print(" ____________________________________________")
    print("|                                            |")
    print("|    ____________________________________    |_")
    print("|   |                                    |   |_)")
    print("|   |   8         4         2         1  |   |")
    print("|   |                                    |   |")
    print("|   |   ",end="")
    if h8==1:print("o         ",end="")
    else:print("          ",end="")
    if h4==1:print("o         ",end="")
    else:print("          ",end="")
    if h2==1:print("o         ",end="")
    else:print("          ",end="")
    if h==1:print("o  |   |")
    else:print("   |   |")
    print("|   |                                    |   |")
    print("|   |                                    |   |")
    print("|   |   ",end="")
    if m32==1:print("o     ",end="")
    else:print("      ",end="")
    if m16==1:print("o     ",end="")
    else:print("      ",end="")
    if m8==1:print("o     ",end="")
    else:print("      ",end="")
    if m4==1:print("o     ",end="")
    else:print("      ",end="")
    if m2==1:print("o     ",end="")
    else:print("      ",end="")
    if m==1:print("o  |   |")
    else:print("   |   |")

    print("|   |                                    |   |")
    print("|   |   32    16    8     4     2     1  |   |_")
    print("|   |____________________________________|   |_)")
    print("|                                            |")
    print("|____________________________________________|")
    print()

while True:
    try:
        h,m=map(int,input().split(':'))
        printar(h,m)
    except EOFError:break
