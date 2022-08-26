#include <algorithm>
#include <fstream>
#include <iostream>
#include <list>
#include <string>
#include <sstream>
#include <stdlib.h>

using namespace std;

class Graph {
    private:
        int numVertices;
        int numArestas;
        list<int> *adj;

    public:
        Graph(int numVertices, int numArestas);
        void addEdge(int origem, int destino);
        list<int> list_predecessores(int vertex);
        list<int> list_sucessores(int vertex);
        void showAdj();
};

Graph::Graph(int numVertices, int numArestas) {
    this->numVertices = numVertices;
    this->numArestas = numArestas;
    adj = new list<int>[numVertices];
}

void Graph::addEdge(int origem, int destino) {
    adj[origem - 1].push_back(destino);
}

list<int> Graph::list_predecessores(int vertex) {
    list<int> predecessores;
    cout << "\nLista de predecessores:";
    for (int i = 0; i < numVertices; ++i) {
        list<int>::iterator it;
        for (it = adj[i].begin(); it != adj[i].end(); ++it) {
            if (*it == vertex) {
                predecessores.push_back(i + 1);
                cout << " " << i + 1;
            }
        }
    }
    return predecessores;
}

list<int> Graph::list_sucessores(int vertex) {
    list<int> sucessores;
    cout << "\nLista de sucessores:";
    for (int i = 0; i < numVertices; ++i) {
        if ((i + 1) == vertex) {
            list<int>::iterator it;
            for (it = adj[i].begin(); it != adj[i].end(); ++it) {
                sucessores.push_back(*it);
                cout << " " << *it;
            }
        }
    }
    return sucessores;
}

void Graph::showAdj() {
    for (int i = 0; i < numVertices; ++i) {
        list<int>::iterator it;
        cout << "Vertice " << i + 1 << ": ";
        for (it = adj[i].begin(); it != adj[i].end(); ++it) {
            cout << " " << *it;
        }
    }
}

void get_atributes(Graph grafo, int vertex) {
    list<int> lista_sucessores = grafo.list_sucessores(vertex);
    list<int> lista_predecessores = grafo.list_predecessores(vertex);
    cout << "\nGrau de entrada: " << lista_predecessores.size();
    cout << "\nGrau de saída: " << lista_sucessores.size();
}

int main(int argc, char** argv) {
    int a, b;
    ifstream file;
    string arquivo = argv[1];
    string vertice = argv[2];
    int vertex = stoi(vertice);

    file.open(arquivo);
    file >> a >> b;

    Graph grafo(a, b);

    while (file >> a >> b) {
        grafo.addEdge(a, b);
    }

    get_atributes(grafo, vertex);

    return 0;
}