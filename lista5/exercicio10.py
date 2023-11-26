from pilha import Pilha

def palindromo(palavra):
    pilha_palindromo = Pilha()
    palavra = palavra.lower().replace(" ", "")

    for letra in palavra:
        pilha_palindromo.empilhar(letra)

    palavra_invertida = ""
    while not pilha_palindromo.is_vazia():
        palavra_invertida += pilha_palindromo.desempilhar()

    return palavra == palavra_invertida

palavra_teste = "radar"
print(f"a palavra '{palavra_teste}'{"" if palindromo(palavra_teste) else " não"} é um palindromo")
