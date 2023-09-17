import re

VOGAIS = "aeiou"

inp = input("digite uma palavra: ")
# remove espaços e pontuação
texto = re.sub(r'[^A-Za-z]', '', inp).lower()

vogais = 0
for letra in inp:
    if letra in VOGAIS:
        vogais += 1

print(f'a quantidade de vogais é: {vogais}')
