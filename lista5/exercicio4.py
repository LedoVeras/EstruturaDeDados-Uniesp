from fila import Fila

fila_tarefas = Fila(capacidade=6)

tarefas = ["Tarefa1", "Tarefa2", "Tarefa3", "Tarefa4"]

for tarefa in tarefas:
    fila_tarefas.enfileirar(tarefa)

print("tarefas para realizar:")
fila_tarefas.visualizar()

while not fila_tarefas.fila_vazia():
    print(f"tarefa atual: {fila_tarefas.desenfileirar()}")