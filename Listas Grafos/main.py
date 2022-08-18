class Grafo:
    def __init__(self, numVertices: int, numArestas: int, lista_graph: list):
        self.numVertices = numVertices
        self.numArestas = numArestas
        self.relacoes = self.sorting(self.create_relacao(lista_graph))
        self.origem = [x[0] for x in self.relacoes]
        self.destino = [x[1] for x in self.relacoes]
    
    def create_relacao(self, lista_graph: list) -> list:
        relacoes = []
        for i in range(2, len(lista_graph)):
            if i % 2 == 0:
                relacoes.append([lista_graph[i], lista_graph[i + 1]])
        return relacoes
    
    def sorting(self, relacoes: list, situacao: int=0) -> list:
        if situacao == 1:
            relacao_ordenada = sorted(relacoes, key=lambda item: item[1])
            return relacao_ordenada
        relacao_ordenada = sorted(relacoes, key=lambda item: item[0])
        return relacao_ordenada

    def forward_star(self) -> list:
        # Ordenar e criar array de destino e origem -> forward_star
        new_relacao = self.sorting(self.relacoes, 1) # Ordena a relação pelo origem
        origem = [x[0] for x in new_relacao] # Cria o array de origem
        pointer = []
        for i in range(0, len(origem)):
            if i == 0:
                pointer.append(i)
            else:
                if origem[i] != origem[i-1]:
                    pointer.append(i)
        pointer.append(pointer[len(pointer) - 1] + 1)
        return pointer

    def reverse_star(self) -> list:
        # Ordenar e criar array de destino e origem -> reverse_star
        new_relacao = self.sorting(self.relacoes, 1) # Ordena a relação pelo destino
        destino = [x[1] for x in new_relacao] # Cria o array de destino
        pointer = []
        pointer.append(0)
        for i in range(0, len(destino)):
            if i == 0:
                pointer.append(i)
            else:
                if destino[i] != destino[i-1]:
                    pointer.append(i)
        pointer.append(pointer[len(pointer) - 1] + 1)
        return pointer

        # TODO: Receber um vértice e mostrar o grau de saída do mesmo
        def get_grau_saida(self, vertice: int) -> int:
            print('Grau de saida')
        
        # TODO: Receber um vértice e mostrar o grau de entrada do mesmo
        def get_grau_entrada(self, vertice: int) -> int:
            print('Grau entrada')

        # TODO: Receber um vértice e mostrar o conjunto de sucessores do mesmo
        def get_conj_sucessores(self, vertice: int) -> list:
            print('Conjunto sucessores')
        
        # TODO: Receber um vértice e mostrar o conjunto de predecessores do  mesmo
        def get_conj_predecessores(self, vertice: int) -> list:
            print('Conjunto predecessores')
    

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
    dir_name = input('Digite o nome do arquivo (se estiver no mesmo dir) ou coloque o diretorio com o nome do arquivo: ')
    lista_graph = get_graph(dir_name)
    grafo = Grafo(lista_graph[0], lista_graph[1], lista_graph)
    vertice_pesquisa = input('Qual o vértice que irá ser pesquisado? ')

if __name__ == "__main__":
    main()
