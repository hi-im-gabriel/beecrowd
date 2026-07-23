while True:
    rounds = int(input())
    if rounds == 0:
        break

    mark = list(map(int, input().split()))
    leti = list(map(int, input().split()))

    mark_score = sum(mark)
    leti_score = sum(leti)
    mark_bonus_round = None
    leti_bonus_round = None

    for i in range(2, rounds):
        if mark_bonus_round is None and mark[i] == mark[i - 1] == mark[i - 2]:
            mark_bonus_round = i
        if leti_bonus_round is None and leti[i] == leti[i - 1] == leti[i - 2]:
            leti_bonus_round = i

    if mark_bonus_round is not None and (leti_bonus_round is None or mark_bonus_round < leti_bonus_round):
        mark_score += 30
    elif leti_bonus_round is not None and (mark_bonus_round is None or leti_bonus_round < mark_bonus_round):
        leti_score += 30

    if mark_score > leti_score:
        print("M")
    elif leti_score > mark_score:
        print("L")
    else:
        print("T")
