for _ in range(int(input())):
    s=input().split()
    if s[1]=='x':s[1]='*'
    if eval(str(s[0]+s[1]+s[2])) == int(s[4]):print("Eou!")
    else:
        aux=abs(eval(str(s[0]+s[1]+s[2]))-int(s[4]))
        print(f"E{'r'*aux}ou!")
