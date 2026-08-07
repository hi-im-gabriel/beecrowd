while True:
    try:
        n = int(input())
    except EOFError:
        break

    if n == 0:
        break

    permutation = list(map(int, input().split()))

    ambiguous = True
    for i in range(n):
        if permutation[permutation[i] - 1] != i + 1:
            ambiguous = False
            break

    if ambiguous:
        print("ambiguous")
    else:
        print("not ambiguous")
