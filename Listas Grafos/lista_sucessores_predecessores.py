import time
import sys
import re

class Grafo:
    def __init__(self, numVertices: int, numArestas: int):
        self.numVertices = numVertices
        self.numArestas = numArestas
        self.relacao = list()

    def addEdges(self, origin: int, dest: int):
        self.relacao.append([int(origin), int(dest)])

    def sorting(self, lis_relacao: list) -> list:
        relacao_ordenada = sorted(lis_relacao, key=lambda item: item[0]) # Origem
        return relacao_ordenada
    
    def getSucessor(self, vertex: int, lis_relacao: list) -> list:
        list_sucessor = []
        for i in range(0, len(lis_relacao)):
            if lis_relacao[i][0] == vertex:
                list_sucessor.append(lis_relacao[i][1])
        return list_sucessor

    def getPredecessor(self, vertex: int, lis_relacao: list) -> list:
        list_predecessor = []
        for i in range(0, len(lis_relacao)):
            if lis_relacao[i][1] == vertex:
                list_predecessor.append(lis_relacao[i][0])
        return list_predecessor
    
    def get_atributes(self, vertex: int) -> None:
        lis_relacao = self.sorting(self.relacao)
        lista_su = self.getSucessor(vertex, lis_relacao)
        lista_pre = self.getPredecessor(vertex, lis_relacao)
        print("Lista de sucessores: " + str(lista_su))
        print("Lista de predecessores: " + str(lista_pre))
        print("Grau da saída: " + str(len(lista_su)))
        print("Grau da entrada: " + str(len(lista_pre)))

def get_graph(arquivo : str) -> list:
    arq = open(arquivo, 'r')
    content = arq.readlines()
    content = [re.sub(' +', ' ', line.strip()) for line in content]
    return content

def main():
    start = time.time() # Get start time

    dir_name = sys.argv[1] # Get dir_name for command line
    vertice_pesquisa = sys.argv[2] # Get vertice_pesquisa for command line

    lista_graph = get_graph(dir_name)
    dados_aresta_vertice = list(lista_graph[0].split(' '))
    grafo = Grafo(dados_aresta_vertice[0], dados_aresta_vertice[1])

    for i in range(1, len(lista_graph)):
        origem_destino = list(lista_graph[i].split(' '))
        grafo.addEdges(origem_destino[0], origem_destino[1])

    grafo.get_atributes(int(vertice_pesquisa))
    
    end = time.time() # Finally get end of the program
    print('Tempo de execução: %.2f segundos.' % (end - start))

if __name__ == "__main__":
    main()
