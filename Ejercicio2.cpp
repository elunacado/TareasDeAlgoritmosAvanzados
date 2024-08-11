#include <iostream>
#include <cmath>

using namespace std;

float PI = 3.1416;

float radioBase, altura, mlPorBotella;

int main() {
    cout << "Ingresa el radio de la base de la maquina en metros: ";
    cin >> radioBase;
    cout << "Ingresa la altura de la maquina en metros: ";
    cin >> altura;
    cout << "Ingresa los mililitros por botella: ";
    cin >> mlPorBotella;

    float volumenCilindro = PI * pow(radioBase, 2) * altura;

    float volumenMl = volumenCilindro * 1000000;
    
    int cantidadRefrescos = volumenMl/mlPorBotella;
    

    cout << "La maquina llena un total de " << cantidadRefrescos << " refrescos" << endl;
    cout << " ";

    return 0;
}