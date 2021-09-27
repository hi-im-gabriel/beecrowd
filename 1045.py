a,b,c=map(float,input().split())
if a<b:a,b=b,a
if b<c:b,c=c,b
if a<b:a,b=b,a
if a>=b+c:print("NAO FORMA TRIANGULO")
elif a*a==b*b+c*c:print("TRIANGULO RETANGULO")
elif a*a>b*b+c*c:print("TRIANGULO OBTUSANGULO")
elif a*a<b*b+c*c:print("TRIANGULO ACUTANGULO")
if a==b==c:print("TRIANGULO EQUILATERO")
elif a==b or b==c or c==a:print("TRIANGULO ISOSCELES")
