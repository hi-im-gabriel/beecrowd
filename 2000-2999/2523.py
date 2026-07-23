1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
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
