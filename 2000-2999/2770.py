while True:
    try:
        a,l,t=map(int,input().split())
        for i in range(t):
            api,lpi=map(int,input().split())
            print("Sim") if (api<=a and lpi<=l) or (api<=l and lpi<=a) else print("Nao")
    except EOFError:break
