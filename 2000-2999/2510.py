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
x = input()
x = int(x)
while(x>=1):
    string = input()
    compr = len(string)
    if(0<=compr and compr <= 25):
        print("Y")
    else:
        print("N")
    x=x-1
