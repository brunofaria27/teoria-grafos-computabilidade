import numpy as np

class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def add_vertice(self, qnt_vertices):
        for i in range(0, qnt_vertices):
            self.vertices.append(i + 1)
    
    def add_relacoes(self, A, B):
        self.arestas.append([A, B])
    
    def gerar_matrizI(self):
        matrizInc = np.zeros((len(self.vertices), len(self.arestas)))
        for j in range(0, len(self.arestas)):
            matrizInc[self.arestas[j][0] - 1][j] = 1
            matrizInc[self.arestas[j][1] - 1][j] = 1
        return matrizInc

    def gerar_matrizA(self):
        matrizAdj = np.zeros((len(self.vertices), len(self.vertices)))
        for j in range(0, len(self.arestas)):
            matrizAdj[self.arestas[j][0] - 1][self.arestas[j][1] - 1] = 1
            matrizAdj[self.arestas[j][1] - 1][self.arestas[j][0] - 1] = 1 # Não direcionado -> tem relação X -> Y e Y -> X
        return matrizAdj
                    
def main():
    grafos = Grafo()
    qnt_vertices = int(input())
    grafos.add_vertice(qnt_vertices)
    qnt_relacoes = int(input())
    for _ in range(0, qnt_relacoes):
        relacao = input().split(' ')
        grafos.add_relacoes(int(relacao[0]), int(relacao[1]))
    print(grafos.gerar_matrizI())
    print(grafos.gerar_matrizA())

if __name__ == "__main__":
    main()