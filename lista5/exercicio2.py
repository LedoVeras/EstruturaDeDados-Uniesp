from fila import Fila

fila_atendimento = Fila(capacidade=5)

clientes = ["cliente1", "cliente2", "cliente3", "cliente4"]

for cliente in clientes:
    fila_atendimento.enfileirar(cliente)

print(f"fila de Atendimento")
fila_atendimento.visualizar()

print("começando o atendimento")

while not fila_atendimento.fila_vazia():
    print(f"atendendo agora: {fila_atendimento.desenfileirar()}")