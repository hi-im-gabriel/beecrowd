import math

n = int(input())

x = ( ( (1 + math.sqrt(5)) / 2)**n - ( ( 1 - math.sqrt(5) ) / 2)**n  ) / math.sqrt(5)

print('%.1f' %x)
