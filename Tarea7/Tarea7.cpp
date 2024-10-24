#include <iostream>
#include <vector>
using namespace std;

#define INF 99999

int V; // Declarar V globalmente

int distanciaMinima(int dist[], bool sptSet[]) {
    int min = INF, min_index = -1;

    for (int v = 0; v < V; v++) {
        if (!sptSet[v] && dist[v] <= min) {
            min = dist[v];
            min_index = v;
        }
    }
    return min_index;
}

void dijkstra(vector<vector<int>>& grafo, int src, int dist[]) {
    bool sptSet[V];

    for (int i = 0; i < V; i++) {
        dist[i] = INF;
        sptSet[i] = false;
    }

    dist[src] = 0;

    for (int count = 0; count < V - 1; count++) {
        int indiceMasCercano = distanciaMinima(dist, sptSet);
        sptSet[indiceMasCercano] = true;

        for (int v = 0; v < V; v++) {
            if (!sptSet[v] && grafo[indiceMasCercano][v] != -1 && dist[indiceMasCercano] != INF && dist[indiceMasCercano] + grafo[indiceMasCercano][v] < dist[v]) {
                dist[v] = dist[indiceMasCercano] + grafo[indiceMasCercano][v];
            }
        }
    }
}

void printDistances(int dist[], int src) {
    cout << "Distancia desde el vertice " << src << endl;
    for (int i = 0; i < V; i++) {
        cout << "To node " << i << ": " << dist[i] << endl;
    }
    cout << endl;
}

int main() {
    cout << "Enter the number of vertices in the graph: ";
    cin >> V;

    vector<vector<int>> graph(V, vector<int>(V, 0));

    cout << "Enter the adjacency matrix (enter -1 if there's no direct path):\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            cout << "Edge from " << i << " to " << j << ": ";
            cin >> graph[i][j];
        }
    }

    for (int i = 0; i < V; i++) {
        int dist[V];
        cout << "\nCalculating shortest paths from vertex " << i << "...\n";
        dijkstra(graph, i, dist);
        printDistances(dist, i);
    }

    return 0;
}