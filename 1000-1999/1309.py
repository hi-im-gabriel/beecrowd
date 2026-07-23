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
#n= list(map(int,input().split()))
while True:
    try:
        mon = '$'
        temp = ''
        dolar = input()
        j = 1
        for t, i in enumerate(reversed(dolar)):
            temp += i
            if(((t+1)%3 == 0) and (t != len(dolar)-1)):
                temp += ','
            j += 1
        mon += temp[::-1]
        cent = input()
        if(len(cent) < 2):
            cent += '0'
            cent = cent[::-1]
        mon += '.' + cent
        print(mon)
        
    except EOFError:
        break
