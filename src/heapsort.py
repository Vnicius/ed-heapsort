import sys


class Heapsort:
    """
    Classe usada para ordenar um vetor utilizando o algoritmo
    de Heapsort

    ...

    Methods
    ---
    sort(vector=list)
        Ordena uma lista de valores

    __build_max_heap(vector=list)
        Constroí a max heap no vetor desordenado

    __heapify(vector=list, root=int, last=int)
        Garante que o vetor está em max heap
    """

    def sort(self, vector):
        """
        Ordena uma lista de valores

        Parameters
        ---
        vector: list
            Uma lista de valores inteiros ou float

        """
        # constroí a max heap a partir do vertor original
        self.__build_max_heap(vector)
        size = len(vector) - 1

        for s in range(size, -1, -1):
            self.__heapify(vector, 0, s)
            vector[0], vector[s] = vector[s], vector[0]

    def __build_max_heap(self, vector):
        """
        Constroí a max heap no vetor desordenado

        Parameters
        ---
        vector: list
            Uma lista de valores inteiros ou float
        """
        size = len(vector) - 1

        for n in range(size//2, -1, -1):
            self.__heapify(vector, n, size)

    def __heapify(self, vector, root, last):
        """
        Garante que o vetor está em max heap

        Parameters
        ---
        vector: list
            Uma lista de valores inteiros ou float

        root: int
            Índice do elemento pai

        last: int
            Índice do último elemento válido do vetor
        """
        left = root * 2 + 1
        right = root * 2 + 2
        largest = root

        # verifica se o filho da esquerda é o maior
        if left <= last and vector[left] > vector[largest]:
            largest = left

        # verifica se o filho da direita é o maior
        if right <= last and vector[right] > vector[largest]:
            largest = right

        # coloca o maior na raíz
        if largest != root:
            vector[root], vector[largest] = vector[largest], vector[root]

            # controí o max heap a partir da nova posição da raíz
            self.__heapify(vector, largest, last)


if __name__ == '__main__':
    ipt = input('Vector: ')
    while ipt != '':
        # divide os valores por ','
        input_vector = ipt.replace(' ', '').split(',')
        values = []
        hs = Heapsort()

        # converte os valores em string para int ou float
        for x in input_vector:
            try:
                values.append(int(x))
            except ValueError:
                try:
                    values.append(float(x))
                except:
                    sys.exit()

        # ordena os valores
        hs.sort(values)
        print(','.join([str(v) for v in values]))
        ipt = input('Vector: ')
