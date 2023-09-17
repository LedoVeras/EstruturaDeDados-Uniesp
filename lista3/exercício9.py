def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "divisão por zero"
    return a / b

print("""Escolha uma operação:"
1. Adição
2. Subtração
3. Multiplicação
4. Divisão""")

operacoes = {'1' : somar,
             '2' : subtrair,
             '3' : multiplicar,
             '4' : dividir}

#roda o código novamente se a escolha for inválida
while(True):
    escolha = input("Digite o número da operação: ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("primeiro número: "))
        num2 = float(input("segundo número: "))

        print(f"resultado: {operacoes[escolha](num1, num2)}")
    else:
        print("opção invalida.")
        continue
    
    break
