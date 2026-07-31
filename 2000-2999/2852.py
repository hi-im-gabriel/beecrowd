key = input()
n = int(input())
vowels = "aeiou"

for _ in range(n):
    words = input().split(" ")
    key_index = 0
    encrypted_words = []

    for word in words:
        if word and word[0] not in vowels:
            encrypted = []
            for letter in word:
                shift = ord(key[key_index % len(key)]) - ord("a")
                encrypted.append(chr((ord(letter) - ord("a") + shift) % 26 + ord("a")))
                key_index += 1
            encrypted_words.append("".join(encrypted))
        else:
            encrypted_words.append(word)

    print(" ".join(encrypted_words))
