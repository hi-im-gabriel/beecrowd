n=int(input())
x=list(map(int,input().split()))
do=[n for n in x if n%2==0]
tr=[n for n in x if n%3==0]
qu=[n for n in x if n%4==0]
ci=[n for n in x if n%5==0]
print(f"{len(do)} Multiplo(s) de 2\n{len(tr)} Multiplo(s) de 3\n{len(qu)} Multiplo(s) de 4\n{len(ci)} Multiplo(s) de 5")
