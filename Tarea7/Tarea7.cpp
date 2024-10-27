#include <iostream>
#include <vector>
using namespace std;

#define INF 99999

int numVertices; // Número de vértices en el grafo

int findMinDistance(int distances[], bool processedSet[]) {
    int minDistance = INF, minIndex = -1;

    for (int vertex = 0; vertex < numVertices; vertex++) {
        if (!processedSet[vertex] && distances[vertex] <= minDistance) {
            minDistance = distances[vertex];
            minIndex = vertex;
        }
    }
    return minIndex;
}

void dijkstra(vector<vector<int>>& graph, int source, int distances[]) {
    bool processedSet[numVertices];

    for (int i = 0; i < numVertices; i++) {
        distances[i] = INF;
        processedSet[i] = false;
    }

    distances[source] = 0;

    for (int count = 0; count < numVertices - 1; count++) {
        int nearestIndex = findMinDistance(distances, processedSet);
        processedSet[nearestIndex] = true;

        for (int vertex = 0; vertex < numVertices; vertex++) {
            if (!processedSet[vertex] && graph[nearestIndex][vertex] != -1 && distances[nearestIndex] + graph[nearestIndex][vertex] < distances[vertex]) {
                distances[vertex] = distances[nearestIndex] + graph[nearestIndex][vertex];
            }
        }
    }
}

void printDistances(int distances[], int source) {
    cout << "\n\nDistancia desde el vértice " << (source + 1) << endl;
    for (int i = 0; i < numVertices; i++) {
        if (source != i) {
            cout << "To node " << (i + 1) << ": " << distances[i] << endl;
        }
    }
}

vector<vector<int>> floyd(vector<vector<int>>& graph) {
    vector<vector<int>> distances = graph;

    for(int i = 0; i < graph.size(); i++){
        for(int j = 0; j < graph[i].size(); j++){
            if(graph[i][j] == -1){
                distances[i][j] = INF;
            } if(i == j){
                distances[i][j] = 0;
            }
        }
    }

    for (int k = 0; k < numVertices; k++) {
        for(int i = 0; i < numVertices; i++){
            for(int j = 0; j < numVertices; j++){
                if (distances[i][j] > (distances[i][k] + distances[k][j])
                    && (distances[k][j] != INF
                        && distances[i][k] != INF))
                    distances[i][j] = distances[i][k] + distances[k][j];
            }
        }
    }

    return distances;

}

int main() {
    cout << "Ingresa el número de vértices en el grafos: ";
    cin >> numVertices;

    vector<vector<int>> graph(numVertices, vector<int>(numVertices, 0));

    cout << "Ingresa la matriz de adyacencia (ingresa -1 si no hay un camino directo):\n";
    for (int i = 0; i < numVertices; i++) {
        for (int j = 0; j < numVertices; j++) {
            cin >> graph[i][j];
        }
    }

    cout << "\nAlgoritmo Dijkstra: \n";
    for (int i = 0; i < numVertices; i++) {
        int distances[numVertices];
        dijkstra(graph, i, distances);
        printDistances(distances, i);
    }

    vector<vector<int>> floydDistances = floyd(graph);
    cout << "\nAlgoritmo Floyd-Warshall: \n";
    for(int i = 0; i < floydDistances.size(); i++){
        for(int j = 0; j < floydDistances[i].size(); j++){
            if(floydDistances[i][j] == INF) {
                cout << "INF ";
            } else {
                cout << floydDistances[i][j] << " ";
            }
        }
        cout << endl;
    }

    return 0;
}
