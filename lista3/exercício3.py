import re

inp = input("Digite uma palavra ou frase: ")

# remove espaços e pontuação
texto = re.sub(r'[^A-Za-z]', '', inp) 

print( ( "não " if texto != texto[::-1] else "" ) +  "é um palíndromo.")
