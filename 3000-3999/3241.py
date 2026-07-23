#n= list(map(int,input().split()))
#string.split('+',2)

n=int(input())

while n:
    string=input()
    if string=="P=NP":
        print("skipped")
    else:
        a,b=string.split('+',2)
        print(int(a)+int(b))

    n-=1
