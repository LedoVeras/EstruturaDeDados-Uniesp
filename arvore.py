class No:
    def __init__(self, chave):
        self.chave = chave
        self.filho1 = None
        self.filho2 = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def incluir(self, chave):
        self.raiz = self._incluir(self.raiz, chave)

    def _incluir(self, no, chave):
        if no is None:
            return No(chave)

        if no.filho1 is None:
            no.filho1 = self._incluir(no.filho1, chave)
        elif no.filho2 is None:
            no.filho2 = self._incluir(no.filho2, chave)
        else:
            # Se ambos os filhos existem, adiciona à folha mais à direita
            no.filho2 = self._incluir(no.filho2, chave)

        return no

    def localizar(self, chave):
        return self._localizar(self.raiz, chave)

    def _localizar(self, no, chave):
        if no is None or no.chave == chave:
            return no
        if chave < no.chave:
            return self._localizar(no.filho1, chave)
        else:
            return self._localizar(no.filho2, chave)

    def visualizar(self):
        self._visualizar(self.raiz)

    def _visualizar(self, no):
        if no is not None:
            self._visualizar(no.filho1)
            print(no.chave, end=" ")
            self._visualizar(no.filho2)