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
33
34
35
36
37
38
39
40
41
42
43
class Toy:
    def __init__(self):
        self.time = 0
        self.points = 0
        self.pointTimeRatio = 0.0
def compare(a, b):
    if a.pointTimeRatio == b.pointTimeRatio:
        return 0
    elif a.pointTimeRatio > b.pointTimeRatio:
        return -1
    else:
        return 1
instance = 0
while True:
    numAttractions, timeLimit = map(int, input().split())
    if numAttractions == 0:
        break
    toys = [Toy() for _ in range(numAttractions)]
    for i in range(numAttractions):
        toys[i].time, toys[i].points = map(int, input().split())
        toys[i].pointTimeRatio = toys[i].points / toys[i].time
    toys.sort(key=lambda x: x.pointTimeRatio, reverse=True)
    i = 0
    totalPoints = totalTime = 0
    while i < numAttractions:
        aux = totalTime + toys[i].time
        if aux <= timeLimit:
            totalPoints += toys[i].points
            totalTime = aux
        else:
            i += 1
    instance += 1
    print(f"Instancia {instance}\n{totalPoints}\n")
