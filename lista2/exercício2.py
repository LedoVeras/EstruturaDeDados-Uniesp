class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        return f"o titulo do livro: {self.titulo}\n e é do autor: {self.autor}"
