while True:
    try:
        string=input()
        tam=len(string)
        for i in range(tam):
            if string[i]=='(':e+=1
            elif string[i]==')':
                d+=1
                if e>0:
                    e-=1
                    d-=1
        print("correct") if e==0 and d==0 else print("incorrect")        
    except EOFError:break
