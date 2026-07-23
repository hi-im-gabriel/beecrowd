data = list(map(int, input().split()))
n, m = data[0], data[1]
houses = data[2:2 + n]
deliveries = data[2 + n:2 + n + m]
positions = {house: index for index, house in enumerate(houses)}

current = 0
total = 0

for house in deliveries:
    destination = positions[house]
    total += abs(destination - current)
    current = destination

print(total)
