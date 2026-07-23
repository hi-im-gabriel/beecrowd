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
24
25
26
27
28
29
30
#n= list(map(int,input().split()))
#string.split('+',2)
#import re re.sub("[^0-9]",""", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")
n=int(input())
while n:
    placa = input().split("-")
    if (len(placa) == 2) and (len(placa[0]) == 3) and (len(placa[1]) == 4) and (placa[0][0]>= 'A') and (placa[0][0]<='Z') and placa[0][1]>='A' and placa[0][1] <='Z' and placa[0][2] >='A' and placa[0][2] <= 'Z':
        try:
            check = int(placa[1])
            r = int(placa[1][3])
            if r > 8 or r == 0:
                print("FRIDAY")
            elif r > 6:
                print("THURSDAY")
            elif r > 4:
                print("WEDNESDAY")
            elif r > 2:
                print("TUESDAY")
            else:
                print("MONDAY")
        except:
            print("FAILURE")
    else:
        print("FAILURE")
    n-=1
