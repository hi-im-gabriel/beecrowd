from decimal import Decimal

while True:
    v_text, n_text, m_text = input().split()
    n = int(n_text)
    m = int(m_text)

    if Decimal(v_text) == 0 and n == 0 and m == 0:
        break

    if n % 10000 == m % 10000:
        multiplier = 3000
    elif n % 1000 == m % 1000:
        multiplier = 500
    elif n % 100 == m % 100:
        multiplier = 50
    elif ((n % 100 - 1) % 100) // 4 == ((m % 100 - 1) % 100) // 4:
        multiplier = 16
    else:
        multiplier = 0

    prize = Decimal(v_text) * multiplier
    print(f"{prize:.2f}")
