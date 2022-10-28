import random

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = list()
    
    def addEdges(self, u, v):
        self.graph.append([u, v])

    '''
    Um grafo eureliano é um grafo onde todos os vértices possuem grau par.
    - Para a execução desse código o intuito é ligar o o primeiro com o segundo o segundo com terceiro, assim por diante.
    - Quando chegar no último vértice fazer ele ligar no primeiro vértice.
    '''
    def eurelianGraph(self):
        for i in range(0, (self.num_vertices - 1)):
            self.addEdges(i, i + 1)
        self.addEdges((self.num_vertices - 1), 0)

    '''
    Um grafo semi-eureliano é um grafo que tem apenas dois vértices de grau ímpar.
    - Cria um grafo eureliano e sorteia uma aresta aleatória para transformar dois vértices de grau par em ímpar.
    '''
    def semiEurelianGraph(self):
        self.eurelianGraph()
        randomEdgeU = random.randint(0, (self.num_vertices - 1))
        randomEdgeV = random.randint(0, (self.num_vertices - 1))
        while randomEdgeU == randomEdgeV:
            randomEdgeU = random.randint(0, (self.num_vertices - 1))
            randomEdgeV = random.randint(0, (self.num_vertices - 1))
        self.addEdges(randomEdgeU, randomEdgeV)

    '''
    Um grafo não eureliano é um grafo que não tem as condições iguais ao eureliano e semi-eureliano
    - Cria um grafo eureliano e sorteia duas arestas para transformar 4 vértices em grau ímpar.
    '''
    def notEurelianGraph(self):
        self.eurelianGraph()
        randomEdgeU = random.randint(0, (self.num_vertices - 1))
        randomEdgeV = random.randint(0, (self.num_vertices - 1))
        randomEdgeUy = random.randint(0, (self.num_vertices - 1))
        randomEdgeVy = random.randint(0, (self.num_vertices - 1))
        while randomEdgeU == randomEdgeV or randomEdgeUy == randomEdgeVy and (randomEdgeU, randomEdgeV) != (randomEdgeUy, randomEdgeVy):
            randomEdgeU = random.randint(0, (self.num_vertices - 1))
            randomEdgeV = random.randint(0, (self.num_vertices - 1))
            randomEdgeUy = random.randint(0, (self.num_vertices - 1))
            randomEdgeVy = random.randint(0, (self.num_vertices - 1))
        self.addEdges(randomEdgeU, randomEdgeV)
        self.addEdges(randomEdgeUy, randomEdgeVy)

    def printGraph(self):
        for i in range(0, len(self.graph)):
            print(self.graph[i])
