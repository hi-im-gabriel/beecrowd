s = input().strip()

pending = 0
for char in s:
    if char == '(':
        pending += 1
    elif pending > 0:
        pending -= 1

if pending > 0:
    print(f"Ainda temos {pending} assunto(s) pendente(s)!")
else:
    print("Partiu RU!")
