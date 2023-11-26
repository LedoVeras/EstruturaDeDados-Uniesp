from fila import Fila

fila_pedidos = Fila(capacidade=8)

pedidos = ["Pedido1", "Pedido2", "Pedido3", "Pedido4"]

for pedido in pedidos:
    fila_pedidos.enfileirar(pedido)

print("pedidos:")
fila_pedidos.visualizar()

while not fila_pedidos.fila_vazia():
    print(f"pedido atual: {fila_pedidos.desenfileirar()}")