dictionary = {}

n = int(input())

for _ in range(n):
    lang = input()
    string = input()
    dictionary[lang] = string

m = int(input())

for _ in range(m):
    name = input()
    lang = input()
    
    print(name)
    print(dictionary.get(lang))
    print()
