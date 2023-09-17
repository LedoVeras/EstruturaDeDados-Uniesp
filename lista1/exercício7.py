inp = input("Digite um número positivo sem casas decimais: \n").strip()

number = abs(int(inp))

prev_fibo = 0
fibo = 1

while(fibo < number):
    next_fibo = prev_fibo + fibo
    if(next_fibo > number):
        break
    
    prev_fibo = fibo
    fibo = next_fibo
    
print(f"o fibonacci mais próximo desse numero é: {fibo}")