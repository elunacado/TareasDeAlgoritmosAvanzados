//Tarea del Merge Sort
//21/08/2024

#include <iostream>
#include <vector>

using namespace std;

void merge(vector<double>& theVector, int left, int mid, int right) {
    //numeros de valores en en el vector de la derecha y el numero de valores en el vector de la izquierda
    int numberOFValuesInLeftVector = mid - left + 1;
    int numberOFValuesInRightVector = right - mid;

    //definimos los vectores de la izquierda y de la derecha
    vector<double> leftVector(numberOFValuesInLeftVector);
    vector<double> rightVector(numberOFValuesInRightVector);

    //Copiemos los valores del lado izquierdo y derecho a los sub vectores designados 
    for (int i = 0; i < numberOFValuesInLeftVector; i++) leftVector[i] = theVector[left + i];
    for (int j = 0; j < numberOFValuesInRightVector; j++) rightVector[j] = theVector[mid + 1 + j];

    int i = 0, j = 0, k = left;

    //Mientras haya elementoes en el vector
    while (i < numberOFValuesInLeftVector && j < numberOFValuesInRightVector) {
        //Dependiendo de cual sea el valor mayor se agregara al vector 
        if (leftVector[i] >= rightVector[j]) {
            theVector[k] = leftVector[i];
            i++;
        } else {
            theVector[k] = rightVector[j];
            j++;
        }
        k++;
    }
    //Si ya no hay elementos para procesar con el vector izquierdo
    while (i < numberOFValuesInLeftVector) {
        //copiamos los valores en el vector principal
        theVector[k] = leftVector[i];
        i++;
        k++;
    }
   //Si ya no hay elementos para procesar con el vector izquierdo
    while (j < numberOFValuesInRightVector) {
        //copiamos los valores en el vector principal
        theVector[k] = rightVector[j];
        j++;
        k++;
    }
}

void mergeSort(vector<double>& theVector, int left, int right) {
    //Cuando el valor de la izquierda sea mayor al de la derecha regresare el vector
    //(Esto solo pasa cuando solo haya un valor en el subVector)
    if (left >= right) return;

    //Defino la mitad del vactor o subVector
    int mid = left + (right - left) / 2;

    //llamo el merge sort para la parte de la izquierda incluyendo el medio
    mergeSort(theVector, left, mid);
    //Llamo el merge sort para la parte de la derecha
    mergeSort(theVector, mid + 1, right);

    merge(theVector, left, mid, right);
}

int main() {
    // Recibo el número de valores que tendrá dentro el vector
    int numberOfValuesInTheVector = 0;
    cin >> numberOfValuesInTheVector;

    // Creo el vector con el número de espacios definido anteriormente
    vector<double> theVector(numberOfValuesInTheVector);

    // Lleno el vector con los valores deseados
    for (int i = 0; i < numberOfValuesInTheVector; i++) {
        cin >> theVector[i];
    }

    //Llamo a la función de merge sort con el indice 0 y numero de valores -1 para balancear el inicio en 0
    mergeSort(theVector, 0, numberOfValuesInTheVector - 1);

    //Imprimo el vector ordenado
    cout << "Sorted vector is: \n";
    for (int i = 0; i < numberOfValuesInTheVector; i++)
        cout << theVector[i] << " ";
    cout << endl;

    return 0;
}
