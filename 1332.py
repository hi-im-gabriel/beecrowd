for n in range(int(input())):
    string=input()
    i=0
    if len(string)==5:print("3")
    else:
        if string[0]=='o':i+=1
        if string[1]=='n':i+=1
        if string[2]=='e':i+=1

        print("1") if i>=2 else print("2")
