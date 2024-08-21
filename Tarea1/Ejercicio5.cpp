#include <iostream>
#include <cmath>

 using namespace std;

 int main() {
    float suma = 1;
    int i = 1;

    cout << "Los primeros 15 numeros de la sumatoria indicada son: " << endl;

    for (int numeroActual = 2; numeroActual <= 16; numeroActual++){
        float parteSuma = 0;

        if (numeroActual % 2 == 0) {
            parteSuma = 1 / pow(numeroActual, 2);
        } else {
            parteSuma = 1 / pow(numeroActual, numeroActual);
        }

        suma += parteSuma;
        cout << i << ". " << parteSuma << endl; 
        cout << "La suma hasta el momento es: " << suma << endl;
        cout << endl;
        i++;
    }

    cout << "La suma total de los primeros 15 terminos es: " << suma << endl;
    cout << endl;

    return 0;
}