while True:
    try:
        dance=""
        string=input()
        tam=len(string)
        aux=0
        for i in range(tam):
            if string[i]==" ":dance+=string[i]
            else:
                if aux==0:
                    dance+=string[i].upper()
                    aux=1
                elif aux==1:
                    dance+=string[i].lower()
                    aux=0
        print(dance)
    except EOFError:break
