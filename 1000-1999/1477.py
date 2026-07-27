readline = open(0, "rb").readline
answers = []

while True:
    line = readline()
    while line and not line.strip():
        line = readline()
    if not line:
        break

    n, operations = map(int, line.split())
    size = 4 * n + 5
    homem = [0] * size
    elefante = [0] * size
    rato = [0] * size
    lazy = [0] * size
    homem[1] = n

    def update(node, left, right, first, last):
        if first <= left and right <= last:
            homem[node], elefante[node], rato[node] = (
                rato[node],
                homem[node],
                elefante[node],
            )
            value = lazy[node] + 1
            lazy[node] = 0 if value == 3 else value
            return

        middle = (left + right) >> 1
        child = node << 1
        if homem[child] + elefante[child] + rato[child] == 0:
            homem[child] = middle - left + 1
            homem[child + 1] = right - middle
        pending = lazy[node]

        if pending:
            other = child + 1
            if pending == 1:
                homem[child], elefante[child], rato[child] = (
                    rato[child],
                    homem[child],
                    elefante[child],
                )
                homem[other], elefante[other], rato[other] = (
                    rato[other],
                    homem[other],
                    elefante[other],
                )
            else:
                homem[child], elefante[child], rato[child] = (
                    elefante[child],
                    rato[child],
                    homem[child],
                )
                homem[other], elefante[other], rato[other] = (
                    elefante[other],
                    rato[other],
                    homem[other],
                )
            value = lazy[child] + pending
            lazy[child] = value - 3 if value >= 3 else value
            value = lazy[other] + pending
            lazy[other] = value - 3 if value >= 3 else value
            lazy[node] = 0

        if first <= middle:
            update(child, left, middle, first, last)
        if last > middle:
            update(child + 1, middle + 1, right, first, last)

        homem[node] = homem[child] + homem[child + 1]
        elefante[node] = elefante[child] + elefante[child + 1]
        rato[node] = rato[child] + rato[child + 1]

    def query(node, left, right, first, last):
        if first <= left and right <= last:
            result[0] += homem[node]
            result[1] += elefante[node]
            result[2] += rato[node]
            return

        middle = (left + right) >> 1
        child = node << 1
        if homem[child] + elefante[child] + rato[child] == 0:
            homem[child] = middle - left + 1
            homem[child + 1] = right - middle
        pending = lazy[node]

        if pending:
            other = child + 1
            if pending == 1:
                homem[child], elefante[child], rato[child] = (
                    rato[child],
                    homem[child],
                    elefante[child],
                )
                homem[other], elefante[other], rato[other] = (
                    rato[other],
                    homem[other],
                    elefante[other],
                )
            else:
                homem[child], elefante[child], rato[child] = (
                    elefante[child],
                    rato[child],
                    homem[child],
                )
                homem[other], elefante[other], rato[other] = (
                    elefante[other],
                    rato[other],
                    homem[other],
                )
            value = lazy[child] + pending
            lazy[child] = value - 3 if value >= 3 else value
            value = lazy[other] + pending
            lazy[other] = value - 3 if value >= 3 else value
            lazy[node] = 0

        if first <= middle:
            query(child, left, middle, first, last)
        if last > middle:
            query(child + 1, middle + 1, right, first, last)

    for _ in range(operations):
        command, first, last = readline().split()
        first = int(first)
        last = int(last)
        if command == b"M":
            update(1, 1, n, first, last)
        else:
            result = [0, 0, 0]
            query(1, 1, n, first, last)
            answers.append(
                str(result[0]) + " " + str(result[1]) + " " + str(result[2])
            )

    answers.append("")

print("\n".join(answers))
