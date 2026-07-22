for i in range(int(input(""))):
    j1,j2=input().split()
    if j1==j2:vitoria="De novo!"
    elif j1=="pedra":
        if j2=="tesoura" or j2=="lagarto":vitoria=j1
        else:vitoria=j2
    elif j1=="papel":
        if j2=="pedra" or j2=="Spock":vitoria=j1
        else:vitoria=j2
    elif j1=="tesoura":
        if j2=="lagarto" or j2=="papel":vitoria=j1
        else:vitoria=j2
    elif j1=="lagarto":
        if j2=="Spock" or j2=="papel":vitoria=j1
        else:vitoria=j2
    elif j1=="Spock":
        if j2=="tesoura" or j2=="pedra":vitoria=j1
        else:vitoria=j2
    if vitoria==j1:vitoria="Bazinga!"
    elif vitoria==j2:vitoria="Raj trapaceou!"
    print(f"Caso #{i+1}: {vitoria}")
