def calcular_imc(peso, altura):
    return round(peso / (altura**2) , 2)

peso = float(input("digite o peso em kg: "))
altura = float(input("digite a altura em metros com '.' ao invés de ',': "))

imc = calcular_imc(peso, altura)
print(f'IMC é {imc:.2f}.')
