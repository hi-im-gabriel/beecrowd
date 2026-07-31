from functools import lru_cache

while True:
    try:
        n = int(input())
    except EOFError:
        break

    initial = tuple(map(int, input().split()))
    m = int(input())
    target = tuple(map(int, input().split()))
    reversed_target = target[::-1]

    if sum(initial) != sum(target):
        print("N")
        continue

    @lru_cache(None)
    def possible(tape):
        length = len(tape)

        if length == m:
            return tape == target or tape == reversed_target

        if length < m:
            return False

        for position in range(1, length):
            left_size = position
            right_size = length - position

            folded_left = list(reversed(tape[:position]))
            if left_size >= right_size:
                for i in range(right_size):
                    folded_left[i] += tape[position + i]
            else:
                folded_left.extend(tape[position + left_size:])
                for i in range(left_size):
                    folded_left[i] += tape[position + i]

            if possible(tuple(folded_left)):
                return True

            folded_right = list(reversed(tape[position:]))
            if right_size >= left_size:
                offset = right_size - left_size
                for i in range(left_size):
                    folded_right[offset + i] += tape[i]
            else:
                folded_right.extend(tape[right_size:position])
                for i in range(right_size):
                    folded_right[i] += tape[position - 1 - i]

            if possible(tuple(folded_right)):
                return True

        return False

    print("S" if possible(initial) else "N")
