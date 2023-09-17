inp = input("Digite um número sem casas decimais: \n").strip()

number = abs(int(inp))

fatorial = 1

for i in range(1, number + 1):
    fatorial *= i

print(f"o fatorial desse numero é: {fatorial}")