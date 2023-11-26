from fila import Fila

fila_pedidos_online = Fila(capacidade=7)

pedidos_online = ["notebook", "caderno", "celular"]

for pedido_online in pedidos_online:
    fila_pedidos_online.enfileirar(pedido_online)

print("\nPedidos:")
fila_pedidos_online.visualizar()

while not fila_pedidos_online.fila_vazia():
    print(f"pedido a processar: {fila_pedidos_online.desenfileirar()}")