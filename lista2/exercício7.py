class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        return f"marca: {self.marca}\n modelo: {self.modelo}\n ano: {self.ano}"
