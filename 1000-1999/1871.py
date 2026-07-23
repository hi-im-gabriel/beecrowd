#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input())

while True:
    n,m=input().split()
    string = ""
    soma = int(n)+int(m)
    soma = str(soma)
    tamanho = len(soma)
    soma = list(map(str,soma))
    if n=='0' and m=='0':
        break
    
    i=0
    while i<=tamanho-1:
        if soma[i] != '0':
            string = string+soma[i]
        i+=1
    print(string)
