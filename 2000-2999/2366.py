n, m = map(int, input().split())
positions = list(map(int, input().split()))
positions.append(42195)

can_finish = all(positions[i] - positions[i - 1] <= m for i in range(1, len(positions)))
print('S' if can_finish else 'N')
