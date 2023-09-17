def celsius_para_fahrenheit(celsius):
    return round((celsius * 9/5) + 32 , 2)

def fahrenheit_para_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9 , 2)

#roda o código novamente se a escolha for inválida
while(True):
    escolha = input("escolha a conversão (C2F celsius para fahrenheit, F2C para Fahrenheit para celsius): ").upper()

    if escolha == 'C2F':
        celsius = float(input("digite a temperatura em celsius: "))
        print(f'a temperatura em fahrenheit é {celsius_para_fahrenheit(celsius)}°F.')
    elif escolha == 'F2C':
        fahrenheit = float(input("digite a temperatura em fahrenheit: "))
        print(f'A temperatura em Celsius é {fahrenheit_para_celsius(fahrenheit)}°C.')
    else:
        print("escolha inválida.")
        continue
    
    break
