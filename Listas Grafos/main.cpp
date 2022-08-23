#include <fstream>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <list>

using namespace std;

class Graph {
    private:
        int numVertices;
        int numArestas;
        list<int> *adj;
    public:
        Graph(int numVertices, int numArestas);
        void addEdge(int origem, int destino);
        void showAdj();
};

Graph::Graph(int numVertices, int numArestas) {
    this->numVertices = numVertices;
    this->numArestas = numArestas;
    adj = new list<int>[numVertices];
}

void Graph::addEdge(int origem, int destino) { adj[origem - 1].push_back(destino); }

void Graph::showAdj() {
    for (int i = 0; i < numVertices; ++i) {
        list<int>::iterator it;
        cout << "Vertice " << i + 1 << ": ";
        for (it = adj[i].begin(); it != adj[i].end(); ++it) {
            cout << "-> " << *it;
        }
        cout << endl;
    }
}

int main() {
    int a, b;
    ifstream file;

    file.open("graph-test-100.txt");
    file >> a >> b;

    Graph grafo(a, b);

    while(file >> a >> b) {
      grafo.addEdge(a, b);
    }

    printf("Printando GRAPH:");
    grafo.showAdj();

    return 0;
}