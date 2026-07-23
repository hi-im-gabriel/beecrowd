#n= list(map(int,input().split()))
#string.split('+',2)
#import re re.sub("[^0-9]",""", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")

while True:
    try:
        n=int(input())
        for i in range(1,n+1,2):
            print((n-i)//2 * ' ', end='')
            print('*'*i)
        print(n//2*' ', end = '')
        print('*')
        print(((n//2)-1)*' ', end = '')
        print('***')
        print()

    except EOFError:
        break
