from pilha import Pilha



comandos_executados = Pilha()
comandos_desfeitos = Pilha()

def comando(comando):
    global comandos_desfeitos
    
    print(f"Executando comando: {comando}")
    comandos_executados.empilhar(comando)
    
    # resetar desfeitos ao executar um novo comando
    comandos_desfeitos = Pilha()  
    
def desfazer():
    if not comandos_executados.is_vazia():
        comando_desfeito = comandos_executados.desempilhar()
        print(f"Desfazendo comando: {comando_desfeito}")
        comandos_desfeitos.empilhar(comando_desfeito)

def refazer():
    if not comandos_desfeitos.is_vazia():
        comando_refeito = comandos_desfeitos.desempilhar()
        print(f"Refazendo comando: {comando_refeito}")
        comandos_executados.empilhar(comando_refeito)


comando("Digitei algo")
comando("Apaguei uma linha")
desfazer()
refazer()
desfazer()
comando("Apaguei uma letra")
refazer()