class MaxHeap:
    def __init__(self):
        self.items = [None]  # sentinela na posição 0

    def __repr__(self):
        # Mostra só os elementos válidos (sem o None)
        return f"MaxHeap({self.items[1:]})"

    def topo(self):
        # opcional: consulta sem remover
        return None if len(self.items) <= 1 else self.items[1]

    def inserir(self, valor):
        self.items.append(valor)
        indice_atual = len(self.items) - 1

        while indice_atual > 1:
            indice_pai = self._pai(indice_atual)

            if self.items[indice_atual] > self.items[indice_pai]:
                self._trocar(indice_atual, indice_pai)
                indice_atual = indice_pai
            else:
                break

    def remover(self):
        if len(self.items) <= 1:
            return None

        # Caso com apenas 1 elemento real
        if len(self.items) == 2:
            return self.items.pop()

        valor_raiz = self.items[1]
        self.items[1] = self.items.pop()  # já remove o último e coloca na raiz

        indice_atual = 1
        while self._tem_filho_esquerdo(indice_atual):
            indice_maior_filho = self._obter_indice_maior_filho(indice_atual)

            if self.items[indice_atual] >= self.items[indice_maior_filho]:
                break

            self._trocar(indice_atual, indice_maior_filho)
            indice_atual = indice_maior_filho

        return valor_raiz

    def _filho_esquerdo(self, indice):
        return 2 * indice

    def _filho_direito(self, indice):
        return 2 * indice + 1

    def _pai(self, indice):
        return indice // 2

    def _trocar(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def _tem_filho_esquerdo(self, indice):
        return (2 * indice) < len(self.items)

    def _tem_filho_direito(self, indice):
        return self._filho_direito(indice) < len(self.items)

    def _obter_indice_maior_filho(self, indice):
        indice_esquerdo = self._filho_esquerdo(indice)
        indice_direito = self._filho_direito(indice)

        if not self._tem_filho_direito(indice):
            return indice_esquerdo

        return indice_direito if self.items[indice_direito] > self.items[indice_esquerdo] else indice_esquerdo

class MinHeap:
    def __init__(self):
        self.items = [None]  # sentinela na posição 0

    def __repr__(self):
        # Mostra só os elementos válidos (sem o None)
        return f"MaxHeap({self.items[1:]})"

    def topo(self):
        # opcional: consulta sem remover
        return None if len(self.items) <= 1 else self.items[1]

    def inserir(self, valor):
        self.items.append(valor)
        indice_atual = len(self.items) - 1

        while indice_atual > 1:
            indice_pai = self._pai(indice_atual)

            if self.items[indice_atual] < self.items[indice_pai]:
                self._trocar(indice_atual, indice_pai)
                indice_atual = indice_pai
            else:
                break

    def remover(self):
        if len(self.items) <= 1:
            return None

        # Caso com apenas 1 elemento real
        if len(self.items) == 2:
            return self.items.pop()

        valor_raiz = self.items[1]
        self.items[1] = self.items.pop()  # já remove o último e coloca na raiz

        indice_atual = 1
        while self._tem_filho_esquerdo(indice_atual):
            indice_maior_filho = self._obter_indice_maior_filho(indice_atual)

            if self.items[indice_atual] < self.items[indice_maior_filho]:
                break

            self._trocar(indice_atual, indice_maior_filho)
            indice_atual = indice_maior_filho

        return valor_raiz

    def _filho_esquerdo(self, indice):
        return 2 * indice

    def _filho_direito(self, indice):
        return 2 * indice + 1

    def _pai(self, indice):
        return indice // 2

    def _trocar(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def _tem_filho_esquerdo(self, indice):
        return (2 * indice) < len(self.items)

    def _tem_filho_direito(self, indice):
        return self._filho_direito(indice) < len(self.items)

    def _obter_indice_maior_filho(self, indice):
        indice_esquerdo = self._filho_esquerdo(indice)
        indice_direito = self._filho_direito(indice)

        if not self._tem_filho_direito(indice):
            return indice_esquerdo

        return indice_direito if self.items[indice_direito] < self.items[indice_esquerdo] else indice_esquerdo