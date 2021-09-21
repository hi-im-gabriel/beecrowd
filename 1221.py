import math
def primo(n):
    if n%2 == 0 and n>2:
        return False
    return all(n%i for i in range(3,int(math.sqrt(n))+1, 2))

x=int(input())

for i in range(0,x):
    n=int(input())
    print("Prime") if primo(n) else print("Not Prime")
