import heapq

def inverter_sinal(lista):
    for i in range(len(lista) - 1):
        lista[i] = -lista[i]

    return lista

lista = [0,4,9,52,14,45]
lista = inverter_sinal(lista)   

heapq.heapify(lista)

k = 3
lista_ordenada = []
for i in range(k):
    lista_ordenada.append(heapq.heappop(lista))

inverter_sinal(lista)
print(lista)