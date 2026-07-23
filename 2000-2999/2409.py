A, B, C = map(int, input().split())
H, L = map(int, input().split())

porta = sorted([H, L])

ok = False
for x, y in [(A, B), (A, C), (B, C)]:
    face = sorted([x, y])
    if face[0] <= porta[0] and face[1] <= porta[1]:
        ok = True
        break

print("S" if ok else "N")
