from copy import deepcopy

from create_adjacencyList import sorting
from create_adjacencyList import listaAdjacencia

'''
O código remove uma aresta do grafo, cria a lista de adjacência e confirma se o grafo é conexo ou não usando busca em largura.
Caso a busca retorne False, ele adiciona a aresta removida na lista de pontes e retorna todas as pontes do grafo.
'''
def naive_bridge(grafo):
    pontes = list()
    for i in range(len(grafo)):
        for j in range(len(grafo[i])):
            grafo_aux = deepcopy(grafo)
            del(grafo_aux[i][j])
            if is_connected(grafo_aux) == False:
                pontes.append([i, grafo[i][j]])
                pontes.append([grafo[i][j], i])
    return pontes

'''
O código implementa uma busca em largura em um grafo, verificando se todos os vértices são visitados. 
Se todos os vértices forem visitados, o grafo é conectado.
'''
def is_connected(graph):
    visited = set()
    queue = []
    start = 0
    queue.append(start)
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return len(visited) == len(graph)