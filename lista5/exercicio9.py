from pilha import Pilha

OPERADORES = "+-*/^"

expressao = "(2+3)*(8-9)/(7^3)"
pilha_operadores = Pilha()

for caractere in expressao:
    if caractere in OPERADORES:
        pilha_operadores.empilhar(caractere)

print("operadores: ")
pilha_operadores.imprimir()
