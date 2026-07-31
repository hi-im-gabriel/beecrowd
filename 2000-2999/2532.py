data = list(map(int, open(0, "rb").read().split()))

index = 0
answers = []
infinity = 10**9

while index < len(data):
    n = data[index]
    health = data[index + 1]
    index += 2

    spells = []
    total_damage = 0

    for _ in range(n):
        damage = data[index]
        cost = data[index + 1]
        index += 2

        spells.append((damage, cost))
        total_damage += damage

    if total_damage < health:
        answers.append("-1")
        continue

    answer = infinity
    candidates = []
    candidates_damage = 0

    for damage, cost in spells:
        if damage >= health:
            if cost < answer:
                answer = cost
        else:
            candidates.append((damage, cost))
            candidates_damage += damage

    if candidates_damage >= health:
        orderings = (
            sorted(candidates, key=lambda spell: spell[1] / spell[0]),
            sorted(candidates, key=lambda spell: spell[1]),
            sorted(candidates, reverse=True),
        )

        for ordered_spells in orderings:
            accumulated_damage = 0
            accumulated_cost = 0

            for damage, cost in ordered_spells:
                accumulated_damage += damage
                accumulated_cost += cost

                if accumulated_damage >= health:
                    if accumulated_cost < answer:
                        answer = accumulated_cost
                    break

    candidates = [
        spell
        for spell in candidates
        if spell[1] < answer
    ]

    candidates.sort()

    dp = [0]

    for damage, cost in candidates:
        if cost >= answer:
            continue

        reachable = len(dp) - 1

        if reachable + damage >= health:
            candidate = min(dp[health - damage:]) + cost

            if candidate < answer:
                answer = candidate

        new_reachable = reachable + damage

        if new_reachable >= health:
            new_reachable = health - 1

        if new_reachable > reachable:
            dp += [infinity] * (new_reachable - reachable)

        end = new_reachable + 1
        source_end = end - damage

        dp[damage:end] = [
            current if current < previous + cost else previous + cost
            for current, previous in zip(
                dp[damage:end],
                dp[:source_end],
            )
        ]

    answers.append(str(answer))

print("\n".join(answers))
