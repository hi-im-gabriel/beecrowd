#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input())
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)

while True:
    try:
        string = ""
        alfa=input()
        n=int(input())
        posicoes=input()
        posicoes=posicoes.split(' ',n-1)
        #print(posicoes)
        i=0
        while n:
            string=string+alfa[int(posicoes[i])-1]
            n-=1
            i+=1
        print(string)

    except EOFError:
        break
