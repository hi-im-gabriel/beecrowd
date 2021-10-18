while True:
    linhas,colunas,c=map(int,input().split())
    if linhas==colunas==c==0:break
    print(int(((linhas - 7) * (colunas - 7) + c) / 2))
