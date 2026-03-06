from heap import MaxHeap, MinHeap
import heapq

def heap_sort(lista):
    heap = MinHeap()
    lista_ordenada = []
    for i in lista:
        heap.inserir(i)

    while len(heap.items) > 1:
        lista_ordenada.append(heap.remover)

    return lista_ordenada

print(heap_sort([8,0,4,1,7]))

#Outra alternativa de codigo
heap = heapq

def heap_sort(lista):
    heapq.heapify(lista)
    lista_ordenada = []

    while lista:
        lista_ordenada.append(heapq.heappop(lista))
    return lista_ordenada

print(heap_sort([89,5,47,2,3]))