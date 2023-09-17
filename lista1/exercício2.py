inp = input("Digite um número sem casas decimais: \n").strip()

number = int(inp)

print(f"esse número é " + "par" if number % 2 == 0 else "ímpar")