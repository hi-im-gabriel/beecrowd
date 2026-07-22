import string
from functools import reduce
def res(s):
    return reduce(lambda r, x: r * 26 + x, map(string.ascii_uppercase.index, s), 0)
while True:
    try:
        s=input()
        tmp=res(s)%1000000007
        print(tmp)
    except:break
