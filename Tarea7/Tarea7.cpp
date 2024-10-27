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

int main() {
    cout << "Enter the number of vertices in the graph: ";
    cin >> numVertices;

    vector<vector<int>> graph(numVertices, vector<int>(numVertices, 0));

    cout << "Enter the adjacency matrix (enter -1 if there's no direct path):\n";
    for (int i = 0; i < numVertices; i++) {
        for (int j = 0; j < numVertices; j++) {
            cin >> graph[i][j];
        }
    }

    for (int i = 0; i < numVertices; i++) {
        int distances[numVertices];
        dijkstra(graph, i, distances);
        printDistances(distances, i);
    }

    return 0;
}
