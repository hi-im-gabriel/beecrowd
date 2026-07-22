x, y, z = map(int, input().split())

if x * x == y * y + z * z:
  area = (y + 3 * z / 4) * z / 2
  print(f"AREA = {int(area)}")
else:
  print("Nao eh retangulo!")
