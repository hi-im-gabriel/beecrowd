while True:
    try:
        phrase = input()
    except EOFError:
        break

    if phrase == ".":
        break

    words = phrase.split()
    frequencies = {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    abbreviations = {}

    for word in sorted(frequencies):
        savings = (len(word) - 2) * frequencies[word]

        if savings > 0:
            letter = word[0]
            if letter not in abbreviations or savings > abbreviations[letter][1]:
                abbreviations[letter] = (word, savings)

    abbreviated_phrase = []

    for word in words:
        letter = word[0]
        if letter in abbreviations and abbreviations[letter][0] == word:
            abbreviated_phrase.append(letter + ".")
        else:
            abbreviated_phrase.append(word)

    print(" ".join(abbreviated_phrase))
    print(len(abbreviations))

    for letter in sorted(abbreviations):
        print(f"{letter}. = {abbreviations[letter][0]}")
