line = ""

while True:
    try:
        tokens = input().split()
    except EOFError:
        break

    for token in tokens:
        if token == "<br>":
            print(line)
            line = ""
        elif token == "<hr>":
            if line:
                print(line)
                line = ""
            print("-" * 80)
        elif not line:
            line = token
        elif len(line) + len(token) + 1 <= 80:
            line += " " + token
        else:
            print(line)
            line = token

if line:
    print(line)
