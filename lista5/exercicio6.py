from pilha import Pilha

historico_navegacao = Pilha()

historico_navegacao.empilhar("Pagina1")
historico_navegacao.empilhar("Pagina2")
historico_navegacao.empilhar("Pagina3")

print("histórico")
historico_navegacao.imprimir()

def voltar():
    historico_navegacao.desempilhar()
    print(f"pagina atual: {historico_navegacao.topo()}")
    
    
voltar()

print("histórico")
historico_navegacao.imprimir()