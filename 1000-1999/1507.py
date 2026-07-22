def verifica(string, subsequence):
    matches = 0
    index = 0
    for char in string:
        if char == subsequence[index]:
            matches += 1
            index += 1
            if matches == len(subsequence):
                return True  
    return False

for test in range(int(input())):
    line = input()
    for i in range(int(input())):
        sub = input()
        print("Yes") if verifica(line, sub) else print("No")
