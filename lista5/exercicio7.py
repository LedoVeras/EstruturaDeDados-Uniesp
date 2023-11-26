from pilha import Pilha

def calcular_rpn(expressao:str):
    pilha = Pilha()
    chars = expressao.split(" ")
    
    for char in chars:
        if char.isdigit() or (char[0] == '-' and char[1:].isdigit()):
            pilha.empilhar(int(char))
        elif char in "+-*/^":
            operand2 = pilha.desempilhar()
            operand1 = pilha.desempilhar()
            if char == '+':
                resultado = operand1 + operand2
            elif char == '-':
                resultado = operand1 - operand2
            elif char == '*':
                resultado = operand1 * operand2
            elif char == '/':
                resultado = operand1 / operand2
            elif char == '^':
                resultado = operand1 ** operand2
            pilha.empilhar(resultado)
    return pilha.topo()


expressao = "3 4 + 2 *"
resultado_calculadora = calcular_rpn(expressao)

print(f"resultado de '{expressao}': {resultado_calculadora}")
