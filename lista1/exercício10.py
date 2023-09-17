import random

opcoes = ["Pedra", "Papel", "Tesoura"]

# Solicita a escolha do usuário
print("Escolha uma opção:")
print("1. Pedra")
print("2. Papel")
print("3. Tesoura")

#roda um while para evitar escolhas inválidas
while True:
    num = int(input("digite o número da sua jogada: ")) - 1
    
    if num < 0 or num >= len(opcoes):
        print("escolha invalida")
    else:
        break

cpu = random.randint(0, 2)
print(f"voce: {opcoes[num]}")
print(f"a cpu escolheu: {opcoes[cpu]}")

if num == cpu:
    print("empate")
elif ((num == 0 and cpu == 2) or(num == 1 and cpu == 0) or (num == 2 and cpu == 1)):
    print("voce venceu")
else:
    print("a cpu venceu")

