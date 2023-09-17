class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return round(3.14 * self.raio ** 2 , 3)
