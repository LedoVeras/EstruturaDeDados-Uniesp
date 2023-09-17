nomes = ["Ana", "João", "Maria", "Pedro", "Lúcia", "Carlos", "Sofia", "Miguel", "Laura", "Rafael", "Beatriz", "Gustavo", "Isabela", "Lucas", "Manuela", "Alice", "Daniel", "Lara", "André", "Julia", "Amanda", "Eduardo", "Alexandre"]

lista_A = [nome for nome in nomes if nome[0].casefold() == "a"]

print(f"""as pessoas que começam com letra "A" nessa lita é:{lista_A}""")