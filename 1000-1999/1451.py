1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
while True:
    try:
        text = input()
        length = len(text)
        point = 1
        word = ''
        temp = ''
        
        for letter in range(length):
            char = text[letter]
            
            if char != '[' and char != ']':
                if point:
                    word += char
                else:
                    temp += char
            
            if char == '[':
                if point:
                    point = 0
                else:
                    word = temp + word
                    temp = ''
            elif char == ']':
                point = 1
                word = temp + word
                temp = ''
        if temp:
            word = temp + word
        print(word)
    except EOFError:
        break
