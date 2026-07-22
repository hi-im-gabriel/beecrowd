def find_parent(city, parent):
  if parent[city] == city:
      return city
  return find_parent(parent[city], parent)

def union(c1, c2, parent, rank):
  root_c1 = find_parent(c1, parent)
  root_c2 = find_parent(c2, parent)

  if root_c1 != root_c2:
      if rank[root_c1] < rank[root_c2]:
          parent[root_c1] = root_c2
      elif rank[root_c1] > rank[root_c2]:
          parent[root_c2] = root_c1
      else:
          parent[root_c1] = root_c2
          rank[root_c2] += 1

def count_countries(cities, borders):
  parent = {i: i for i in range(1, cities + 1)}
  rank = {i: 0 for i in range(1, cities + 1)}

  for border in borders:
      c1, c2 = border
      union(c1, c2, parent, rank)

  countries = set()
  for city in range(1, cities + 1):
      countries.add(find_parent(city, parent))

  return len(countries)

# Leitura da entrada
C, F = map(int, input().split())
borders = [tuple(map(int, input().split())) for _ in range(F)]

# Chamada da função e impressão do resultado
result = count_countries(C, borders)
print(result)
