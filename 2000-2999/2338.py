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
36
37
38
39
40
41
42
def translate_message(morse):
    characters = morse.split("...")
    translated_message = ""
    for char in characters:
        translated_message += convert_char(char[1:] if char.startswith(".") else char)
    return translated_message
def convert_char(s):
    char_map = {
        "=.===": 'a',
        "===.=.=.=": 'b',
        "===.=.===.=": 'c',
        "===.=.=": 'd',
        "=": 'e',
        "=.=.===.=": 'f',
        "===.===.=": 'g',
        "=.=.=.=": 'h',
        "=.=": 'i',
        "=.===.===.===": 'j',
        "===.=.===": 'k',
        "=.===.=.=": 'l',
        "===.===": 'm',
        "===.=": 'n',
        "===.===.===": 'o',
        "=.===.===.=": 'p',
        "===.===.=.===": 'q',
        "=.===.=": 'r',
        "=.=.=": 's',
        "===": 't',
        "=.=.===": 'u',
        "=.=.=.===": 'v',
        "=.===.===": 'w',
        "===.=.=.===": 'x',
        "===.=.===.===": 'y',
        "===.===.=.=": 'z',
    }
    return char_map.get(s, ' ')
N = int(input())
for _ in range(N):
    morse = input()
    print(translate_message(morse))
