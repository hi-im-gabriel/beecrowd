while True:
    m = int(input())
    if m == 0:
        break

    p = 2
    cont = 0

    for i in range(m):
        line = input()
        parts = line.split()
        
        if parts == ["0", "1", "1"] and p != 1:
            cont += abs(p - 1)
            p = 1
        elif parts == ["1", "0", "1"] and p != 2:
            cont += abs(p - 2)
            p = 2
        elif parts == ["1", "1", "0"] and p != 3:
            cont += abs(p - 3)
            p = 3

    print(cont)
