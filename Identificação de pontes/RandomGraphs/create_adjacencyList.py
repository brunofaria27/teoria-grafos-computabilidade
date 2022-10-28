def sorting(graph):
    relacao_ordenada = sorted(graph, key=lambda item: item[0])
    return relacao_ordenada

def listaAdjacencia(arestas, vertices):
    listaAdjacencia = [[] for i in range(vertices)] # Inicialização do array
    for i in range(len(arestas)):
        listaAdjacencia[arestas[i][0]].append(arestas[i][1])
        listaAdjacencia[arestas[i][1]].append(arestas[i][0])
    return listaAdjacencia