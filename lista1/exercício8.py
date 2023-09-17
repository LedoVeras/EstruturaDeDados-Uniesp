inp = input("Digite um número positivo sem casas decimais: \n").strip()

num = int(inp)

prime = True

for l in range(2 , num):
    if(num % l == 0):
        prime = False
        break
        
print(num, "" if prime else " nao", " é primo", sep="")