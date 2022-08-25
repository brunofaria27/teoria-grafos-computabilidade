import time
import sys

class Grafo:
    def __init__(self, numVertices: int, numArestas: int, lista_graph: list):
        self.numVertices = numVertices
        self.numArestas = numArestas
        self.relacao = self.sorting(self.create_relacao(lista_graph))

    def create_relacao(self, lista_graph: list) -> list:
        relacoes = []
        for i in range(2, len(lista_graph)):
            if i % 2 == 0:
                relacoes.append([lista_graph[i], lista_graph[i + 1]])
        return relacoes

    def sorting(self, relacoes: list) -> list:
        relacao_ordenada = sorted(relacoes, key=lambda item: item[0]) # Origem
        return relacao_ordenada
    
    def getSucessor(self, vertex: int) -> list:
        list_sucessor = []
        for i in range(0, len(self.relacao)):
            if self.relacao[i][0] == vertex:
                list_sucessor.append(self.relacao[i][1])
        return list_sucessor

    def getPredecessor(self, vertex: int) -> list:
        list_predecessor = []
        for i in range(0, len(self.relacao)):
            if self.relacao[i][1] == vertex:
                list_predecessor.append(self.relacao[i][0])
        return list_predecessor
    
    def get_atributes(self, vertex: int) -> None:
        lista_su = self.getSucessor(vertex)
        lista_pre = self.getPredecessor(vertex)
        print("Lista de sucessores: " + str(lista_su))
        print("Lista de predecessores: " + str(lista_pre))
        print("Grau da saída: " + str(len(lista_su)))
        print("Grau da entrada: " + str(len(lista_pre)))

def get_graph(arquivo : str) -> list:
    arq = open(arquivo, 'r')
    lista_graph = []
    for linha in arq:
        linha = linha.rstrip('\n')
        for i in linha.split(' '):
            try:
                lista_graph.append(int(i))
            except ValueError:
                continue
    return lista_graph

def main():
    start = time.time() # Get start time

    dir_name = sys.argv[1] # Get dir_name for command line
    vertice_pesquisa = sys.argv[2] # Get vertice_pesquisa for command line

    lista_graph = get_graph(dir_name)
    grafo = Grafo(lista_graph[0], lista_graph[1], lista_graph)
    grafo.get_atributes(int(vertice_pesquisa))
    
    end = time.time() # Finally get end of the program
    print('Tempo de execução: %.2f segundos.' % (end - start))

if __name__ == "__main__":
    main()
