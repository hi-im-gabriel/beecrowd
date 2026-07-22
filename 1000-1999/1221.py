from math import sqrt
def primo(n):
    if n%2==0 and n>2:return False
    return all(n%i for i in range(3,int(sqrt(n))+1, 2))

for i in range(int(input())):
    n=int(input())
    print("Prime") if primo(n) else print("Not Prime")
