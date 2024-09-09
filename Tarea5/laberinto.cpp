#include <iostream>
#include <vector>
using namespace std;

bool esSeguro(const vector<vector<int>> &laberinto, int x, int y, const vector<vector<int>> &solucion){
    int n = laberinto.size();
    return (x >= 0 && x < n && y >= 0 && y < n && laberinto[x][y] == 1 && solucion[x][y] == 0);
}

bool resolverLaberinto(vector<vector<int>> &laberinto, int x, int y, vector<vector<int>> &solucion){
    int n = laberinto.size();

    // Si hemos alcanzado el destino
    if(x == n - 1 && y == n - 1){
        solucion[x][y] = 1;
        return true;
    }

    if(esSeguro(laberinto, x, y, solucion)){
        solucion[x][y] = 1;  // Marca la celda como parte de la solución

        // Moverse hacia abajo
        if(resolverLaberinto(laberinto, x + 1, y, solucion)){
            return true;
        }

        // Moverse hacia la derecha
        if(resolverLaberinto(laberinto, x, y + 1, solucion)){
            return true;
        }

        // Si no se encuentra solución, desmarcar la celda (backtracking)
        solucion[x][y] = 0;
    }
    return false;
}

void imprimirSolucion(vector<vector<int>> solucion){
    int n = solucion.size();
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << solucion[i][j] << " ";
        }
        cout << endl;
    }
}

int main(){
    int n;
    cout << "Ingrese el tamaño del laberinto: ";
    cin >> n;

    vector<vector<int>> laberinto(n, vector<int>(n, 0));

    cout << "Ingrese el laberinto (1 = camino, 0 = obstáculo): " << endl;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << "Ingrese el valor de la casilla (" << i << ", " << j << "): ";
            cin >> laberinto[i][j];
        }
    }

    vector<vector<int>> solucion(n, vector<int>(n, 0)); 

    // Intentar resolver el laberinto
    if(resolverLaberinto(laberinto, 0, 0, solucion)){
        cout << endl << "Solución encontrada:" << endl;
        imprimirSolucion(solucion);
    } else {
        cout << endl << "No se encontró una solución para el laberinto." << endl;
    }

    return 0;
}
