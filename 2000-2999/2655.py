n, q, m = map(int, input().split())
monsters = list(map(int, input().split()))

size = 1
while size < n:
    size *= 2

tree = [0] * (2 * size)
for i, monster_type in enumerate(monsters):
    tree[size + i] = 1 << (monster_type - 1)

for i in range(size - 1, 0, -1):
    tree[i] = tree[2 * i] | tree[2 * i + 1]

for _ in range(q):
    operation, first, second = map(int, input().split())

    if operation == 1:
        left = size + first - 1
        right = size + second
        mask = 0

        while left < right:
            if left % 2 == 1:
                mask |= tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                mask |= tree[right]
            left //= 2
            right //= 2

        print(bin(mask).count("1"))
    else:
        position = size + first - 1
        tree[position] = 1 << (second - 1)
        position //= 2

        while position:
            tree[position] = tree[2 * position] | tree[2 * position + 1]
            position //= 2
