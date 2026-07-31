n, target_attack, target_defense, target_ability = map(int, input().split())
cards = [tuple(map(int, input().split())) for _ in range(n)]


def combinations(part):
    sums = {(0, 0, 0): 0}

    for attack, defense, ability in part:
        new_sums = dict(sums)

        for (sum_attack, sum_defense, sum_ability), count in sums.items():
            next_attack = sum_attack + attack
            next_defense = sum_defense + defense
            next_ability = sum_ability + ability

            if (next_attack <= target_attack and
                    next_defense <= target_defense and
                    next_ability <= target_ability):
                key = (next_attack, next_defense, next_ability)
                new_sums[key] = max(new_sums.get(key, 0), count + 1)

        sums = new_sums

    return sums


middle = n // 2
left_sums = combinations(cards[:middle])
right_sums = combinations(cards[middle:])

possible = False

for (attack, defense, ability), left_count in left_sums.items():
    complement = (
        target_attack - attack,
        target_defense - defense,
        target_ability - ability,
    )

    if complement in right_sums and left_count + right_sums[complement] >= 2:
        possible = True
        break

print("Y" if possible else "N")
