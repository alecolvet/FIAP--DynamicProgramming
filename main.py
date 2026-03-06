from heap import MaxHeap, MinHeap

heap = MinHeap()

heap.inserir(10)
heap.inserir(4)
heap.inserir(15)
heap.inserir(20)
heap.inserir(8)

print("Heap após inserções:")
print(heap)

maior = heap.remover()
print("\nElemento removido:", maior)

print("\nHeap após remoção:")
print(heap)

heap.inserir(30)
heap.inserir(2)

print("\nHeap após novas inserções:")
print(heap)

print("\nRemovendo todos os elementos:")
while True:
    removido = heap.remover()
    if removido is None:
        break
    print("Removido:", removido)