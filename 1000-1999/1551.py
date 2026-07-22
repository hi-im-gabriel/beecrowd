while True:
    try:
        text = input()
        length = len(text)
        point = 1
        word = ''
        temp = ''
        
        for letter in range(length):
            char = text[letter]
            
            if char != '[' and char != ']':
                if point:
                    word += char
                else:
                    temp += char
            
            if char == '[':
                if point:
                    point = 0
                else:
                    word = temp + word
                    temp = ''
            elif char == ']':
                point = 1
                word = temp + word
                temp = ''

        if temp:
            word = temp + word
        print(word)

    except EOFError:
        break
