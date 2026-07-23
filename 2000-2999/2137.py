#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input())
while True:
    try:
        n=int(input())
        aux=n
        string = []
        while n:
            string.append(input())
            n-=1

        inteira=sorted(string)
        i=0
        while i<=aux-1:
            print(inteira[i])
            i+=1
    except EOFError:
        break
