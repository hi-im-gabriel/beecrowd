while True:
    try:
        s=input()
        s=s.replace("O","0").replace("o","0").replace("l","1").replace(",","").replace(" ","")
        if s.isdigit():
            s=int(s)
            if s>2147483647:print("error")
            else:print(s)
        else:print("error")
    except EOFError:
