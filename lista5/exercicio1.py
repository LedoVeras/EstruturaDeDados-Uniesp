from fila import Fila

fila_impressao = Fila(capacidade=10)

documentos = ["pdf1", "panfleto", "pdf2", "A4"]

for doc in documentos:
    fila_impressao.enfileirar(doc)

print(f"fila de impressão : {fila_impressao.visualizar()}")
