inp = input("Digite três numeros divididos por um único espaço: \n").strip().split(" ")

#transforma o array de string em um array de floats
numbers = [float(num) for num in inp]

average = round(sum(numbers) / 3 , 2)

print(f"a média dos números é: {average}")