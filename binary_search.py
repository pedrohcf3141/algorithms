from typing import Union
import time
import sys


def busca_binaria(lista: list, resp: int) -> int:
    tentativa = lista[len(lista) //2]
    cont = 0
    while tentativa != resp:
        tentativa = lista[len(lista)//2]
        if resp < tentativa:
            lista = lista[:lista.index(tentativa)]
        elif resp > tentativa:
            lista = lista[lista.index(tentativa):]
        cont += 1
    return cont


def binary_search(arr: list, resp: int) -> Union[int, None]:
    start = 0
    end = len(arr) -1
    count = 0
    while start <= end:
        middle = (start + end) // 2
        shot = arr[middle]
        if resp == shot:
            return count
        elif resp < shot:
            end = middle - 1
        else:
            start = middle + 1
        count +=1
    return None


def busca_binaria_memoria_tempo(lista: list, resp: int) -> int:
    start_mem = sys.getsizeof(lista)
    start_time = time.time()
    tentativa = lista[len(lista) //2]
    cont = 0
    while tentativa != resp:
        tentativa = lista[len(lista)//2]
        if resp < tentativa:
            lista = lista[:lista.index(tentativa)]
        elif resp > tentativa:
            lista = lista[lista.index(tentativa):]
        cont += 1
    end_time = time.time()
    end_mem = sys.getsizeof(lista)
    print(f"Tempo de execução: {end_time - start_time} segundos")
    print(f"Uso de memória: {end_mem - start_mem} bytes")
    return cont


def binary_search_memory_time(arr: list, resp: int) -> Union[int, None]:
    start_mem = sys.getsizeof(arr)
    start_time = time.time()
    start = 0
    end = len(arr) -1
    count = 0
    while start <= end:
        middle = (start + end) // 2
        shot = arr[middle]
        if resp == shot:
            end_time = time.time()
            end_mem = sys.getsizeof(arr)
            print(f"Time: {end_time - start_time} seconds")
            print(f"Memory: {end_mem - start_mem} bytes")
            return count
        elif resp < shot:
            end = middle - 1
        else:
            start = middle + 1
        count +=1
    return None


"""
A segunda função, binary_search, é mais eficiente em termos de uso de memória e
tempo de execução por vários motivos:

Uso de memória: A função busca_binaria cria novas listas a cada iteração quando
realiza as operações de fatiamento (lista[:lista.index(tentativa)] e
lista[lista.index(tentativa):]). Isso aumenta o uso de memória, pois cada nova
lista criada ocupa espaço na memória. Por outro lado, a função binary_search não
cria novas listas, mas apenas atualiza os índices de início e fim. Isso resulta
em um uso de memória constante, independentemente do tamanho da lista.

Tempo de execução: A função busca_binaria usa o método list.index(), que tem uma
complexidade de tempo de O(n), pois precisa percorrer a lista para encontrar o
índice do elemento. Isso é feito a cada iteração, o que aumenta o tempo de
execução. Em contraste, a função binary_search usa índices para acessar
diretamente os elementos, o que tem uma complexidade de tempo constante de O(1).
Além disso, a função binary_search divide a lista pela metade a cada iteração
(dai o nome “busca binária”), o que resulta em uma complexidade de tempo
logarítmica de O(log n).

Portanto, a função binary_search é mais eficiente tanto em termos de uso de
memória quanto de tempo de execução.

The second function, binary_search, is more efficient in terms of memory usage and
execution time for several reasons:
#----------------------------------------------------------------------------
Memory usage: The busca_binaria function creates new lists at each iteration when
it performs slicing operations (lista[:lista.index(tentativa)] and
lista[lista.index(tentativa):]). This increases memory usage, as each new list
created occupies space in memory. On the other hand, the binary_search function
does not create new lists, but only updates the start and end indices. This results
in constant memory usage, regardless of the size of the list.

Execution time: The busca_binaria function uses the list.index() method, which has a
time complexity of O(n), as it needs to traverse the list to find the index of the
element. This is done at each iteration, which increases the execution time. In
contrast, the binary_search function uses indices to directly access the elements,
which has a constant time complexity of O(1). In addition, the binary_search function
divides the list in half at each iteration (hence the name "binary search"), which
results in a logarithmic time complexity of O(log n).

Therefore, the binary_search function is more efficient both in terms of memory usage
and execution time.
"""
#----------------------------------------------------------------------------
lista = [num for num in range(128)]
resp = lista[0]
print(f"Passos Busca Binaria: {busca_binaria(lista, resp)}")
#----------------------------------------------------------------------------
lista = [num for num in range(128)]
resp = lista[0]
print(f"Passos Busca Binaria: {busca_binaria_memoria_tempo(lista, resp)}")
#----------------------------------------------------------------------------
arr = [num for num in range(1024)]
resp = 132
print(f"Steps Binary Search: {binary_search(arr, resp)}")
#----------------------------------------------------------------------------
arr = [num for num in range(1024)]
resp = 132
print(f"Steps Binary Search: {binary_search_memory_time(arr, resp)}")
#----------------------------------------------------------------------------