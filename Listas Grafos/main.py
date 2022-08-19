class Grafo:
    def __init__(self, numVertices: int, numArestas: int, lista_graph: list):
        self.numVertices = numVertices
        self.numArestas = numArestas
        self.relacoes = self.sorting(self.create_relacao(lista_graph))
    
    def create_relacao(self, lista_graph: list) -> list:
        relacoes = []
        for i in range(2, len(lista_graph)):
            if i % 2 == 0:
                relacoes.append([lista_graph[i], lista_graph[i + 1]])
        return relacoes
    
    def sorting(self, relacoes: list, situacao: int=0) -> list:
        if situacao == 1:
            relacao_ordenada = sorted(relacoes, key=lambda item: item[1]) # Destino
            return relacao_ordenada
        relacao_ordenada = sorted(relacoes, key=lambda item: item[0]) # Origem
        return relacao_ordenada

    def forward_star(self) -> list:
        # Ordenar e criar array de destino e origem -> forward_star
        new_relacao = self.sorting(self.relacoes, 0) # Ordena a relação pelo origem
        origem = [x[0] for x in new_relacao] # Cria o array de origem
        destino_for = [x[1] for x in new_relacao] # Cria o array de destino ordenado com origem
        pointer = []
        for i in range(0, len(origem)):
            if i == 0:
                pointer.append(i)
            else:
                if origem[i] != origem[i - 1]:
                    pointer.append(i)
        pointer.append(len(origem))
        return pointer, origem, destino_for

    def reverse_star(self) -> list:
        # Ordenar e criar array de destino e origem -> reverse_star
        new_relacao = self.sorting(self.relacoes, 1) # Ordena a relação pelo destino
        destino = [x[1] for x in new_relacao] # Cria o array de destino
        origem_rev = [x[0] for x in new_relacao] # Cria o array de origem ordenado com destino
        pointer = []
        pointer.append(0)
        for i in range(1, len(destino)):
            if destino[i] != destino[i - 1]:
                pointer.append(i)
        pointer.append(len(destino))
        return pointer, destino, origem_rev

    def get_conj_sucessores(self, vertice: int, pointer: list, origem: list, destino: list) -> list:
        sucessores = []
        for point in range(0, len(pointer) - 1):
            qnt_nums = pointer[point + 1] - pointer[point]
            if origem[pointer[point]] == vertice:
                for i in range(pointer[point], pointer[point] + qnt_nums):
                    sucessores.append(destino[i])
        return sucessores

    def get_conj_predecessores(self, vertice: int, pointer: list, destino: list, origem_rev: list) -> list:
        predecessores = []
        for point in range(0, len(pointer) - 1):
            qnt_nums = pointer[point + 1] - pointer[point]
            if destino[pointer[point]] == vertice:
                for i in range(pointer[point], pointer[point] + qnt_nums):
                    predecessores.append(origem_rev[i])
        return predecessores

    def get_atributes(self, vertice: int):
        pointer_for, origem, destino_for = self.forward_star()
        pointer_rev, destino, origem_rev = self.reverse_star()
        conjunto_sucessores = self.get_conj_sucessores(vertice, pointer_for, origem, destino_for)
        conjunto_predecessores = self.get_conj_predecessores(vertice, pointer_rev, destino, origem_rev)
        print('Conjunto de sucessores -> ' + str(conjunto_sucessores))
        print('Grau de saída -> ' + str(len(conjunto_sucessores)))
        print('Conjunto de predecessores -> ' + str(conjunto_predecessores))
        print('Grau de entrada -> ' + str(len(conjunto_predecessores)))
    

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
    vertice_pesquisa = int(input('Qual o vértice que irá ser pesquisado? '))
    grafo.get_atributes(vertice_pesquisa)

if __name__ == "__main__":
    main()
