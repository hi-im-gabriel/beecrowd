n,m=map(int,input().split())
if m-n>=3:print("Muito bem! Apresenta antes do Natal!")
elif m-n<0:print("Eu odeio a professora!")
elif m-n<3:
    print("Parece o trabalho do meu filho!")
    m+=2
    if m<=24:print("TCC Apresentado!")
    else:print("Fail! Entao eh nataaaaal!")
