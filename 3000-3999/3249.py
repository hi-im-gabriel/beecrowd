wins = 0
for _ in range(int(input())):
    string = input()
    if not 'CD' in string:
        wins += 1
        
print(wins)
