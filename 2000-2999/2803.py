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
estado = input().strip()
norte = {
    "acre", "amapa", "amazonas",
    "para", "rondonia", "roraima", "tocantins"
}
if estado in norte:
    print("Regiao Norte")
else:
    print("Outra regiao")
