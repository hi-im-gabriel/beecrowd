estado = input().strip()

norte = {
    "acre", "amapa", "amazonas",
    "para", "rondonia", "roraima", "tocantins"
}

if estado in norte:
    print("Regiao Norte")
else:
    print("Outra regiao")
