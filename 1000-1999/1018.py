n=int(input())
print(n)
print(f"{(n/100)} nota(s) de R$ 100,00")
n = n%100
print(f"{(n/50)} nota(s) de R$ 50,00")
n = n%50
print(f"{(n/20)} nota(s) de R$ 20,00")
n = n%20
print(f"{(n/10)} nota(s) de R$ 10,00")
n = n%10
print(f"{(n/5)} nota(s) de R$ 5,00")
n = n%5
print(f"{(n/2)} nota(s) de R$ 2,00")
n = n%2
print(f"{n} nota(s) de R$ 1,00")
