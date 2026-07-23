#n= list(map(int,input().split()))
while True:
    D,N=input().split()
    if D=='0' and N=='0':
        break
    nova = ""
    tamanho = len(N)-1
    i=0
    while(i<=tamanho):
        if N[i] != D:
            nova = nova + N[i]
            
        i+=1
    try:
        nova = int(nova)
    except:
        nova = 0


    print(nova)
