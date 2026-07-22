dodo = "Os atributos dos monstros vao ser inteligencia, sabedoria..."
leo = "Iron Maiden's gonna get you, no matter how far!"
pepper = "Urano perdeu algo muito precioso..."
empate = "Putz vei, o Leo ta demorando muito pra jogar..."
def vence(x, y):
    return (x == 'pedra' and y == 'tesoura') or (x == 'papel' and y == 'pedra') or (x == 'tesoura' and y == 'papel')

while True:
   try:
      d,l,p=input().split()
      if vence(d,p) and vence(d,l):print(dodo)
      elif vence(l,d) and vence(l,p):print(leo)
      elif vence(p,d) and vence(p,l):print(pepper)
      else:print(empate)
   except EOFError:break
