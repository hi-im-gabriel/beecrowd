1
2
3
4
5
6
7
import math
n = int(input())
x = ( ( (1 + math.sqrt(5)) / 2)**n - ( ( 1 - math.sqrt(5) ) / 2)**n  ) / math.sqrt(5)
print('%.1f' %x)
