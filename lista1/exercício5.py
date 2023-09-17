lista = [1 ,2 , 2 , 1 , -1, 5, 6, 1, 8, 5, 6, 9, 2]

pares = [num for num in lista if num % 2 == 0]

average = round(sum(pares) / len(pares), 2)

print(f"a média dos números pares é: {average}")
