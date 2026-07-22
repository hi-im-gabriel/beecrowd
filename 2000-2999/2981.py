c,g=map(int,input().split())
print(f"A UFSC fecha dia {(c//g)+21} de setembro.") if c//g<10 else print(f"A UFSC fecha dia {(c//g)-9} de outubro.")
