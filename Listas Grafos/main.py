class Grafo:
    def __init__(self, numVertices: int, numArestas: int, lista_graph: list):
        self.numVertices = numVertices
        self.numArestas = numArestas
        self.origem = self.create_origem(lista_graph)
        self.destino = self.create_destino(lista_graph)
        self.relacoes = self.create_relacao(lista_graph)
    
    def create_origem(self, lista_graph: list) -> list:
        origem = []
        for i in range(2, len(lista_graph)):
            if i % 2 == 0:
                origem.append(lista_graph[i])
        return origem

    def create_destino(self, lista_graph: list):
        destino = []
        for i in range(2, len(lista_graph)):
            if i % 2 != 0:
                destino.append(lista_graph[i])
        return destino
    
    def create_relacao(self, lista_graph: list) -> list:
        relacoes = []
        for i in range(2, len(lista_graph)):
            if i % 2 == 0:
                relacoes.append([lista_graph[i], lista_graph[i + 1]])
        return relacoes
    
    def forward_star(self):
        print('ORIGEM -> ' + str(self.origem))
        print('DESTINO -> ' + str(self.destino))

    def reverse_star(self):
        print('ORIGEM -> ' + str(self.origem))
        print('DESTINO -> ' + str(self.destino))

    def print_destin_orig(self):
        print('ORIGEM -> ' + str(self.origem))
        print('DESTINO -> ' + str(self.destino))

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
    dir_name = input()
    lista_graph = get_graph(dir_name)
    grafo = Grafo(lista_graph[0], lista_graph[1], lista_graph)
    #
    grafo.forward_star()


if __name__ == "__main__":
    main()
