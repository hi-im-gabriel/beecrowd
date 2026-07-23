1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
from sys import stdin
from math import ceil
def minimum_number_pages(story, max_lines, max_char):
    max_char_counter = 0
    pages = 0
    lines = 1
    for s in story.split():
        if len(s) + max_char_counter <= max_char:
            max_char_counter += len(s) + 1
        else:
            max_char_counter = 0
            max_char_counter += len(s) + 1
            lines += 1
    return ceil(lines/max_lines)
while True:
    ln = stdin.readline().split()
    if not ln:
        break 
    n, max_lines, max_char = map(int, ln)
    story = stdin.readline()
    print(minimum_number_pages(story, max_lines, max_char))
