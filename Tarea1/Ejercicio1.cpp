//Problema de las Camisas
//Autor: Ethan Luna Cadó
//Fecha: 08/08/2024

/*
En una maquila, un supervisor de producción registra la cantidad de producto terminado
(camisas) que cada línea de producción genera durante un día completo de trabajo. Se
tienen 2 líneas de producción que, por diversas razones, no necesariamente producen la
misma cantidad diaria del producto.

Se desea tener un programa que permita saber en cuantos días es posible surtir un pedido
de N camisas. Con la intención de mejorar la planeación de los tiempos de entrega y de los
insumos necesarios para producirlas ya que últimamente se han registrado retrasos en los
tiempos de entrega
*/

using namespace std;
#include <iostream>

int maquina1 = 0;
int maquina2 = 0;
int tamanioDelPedido;
int dias = 1;

int calcularDias(int maquina1, int maquina2, int dias, int totalProducidas = 0){
    totalProducidas +=  maquina1 + maquina2;
    if (totalProducidas >= tamanioDelPedido){
        return dias;
    } else{
        return calcularDias(maquina1, maquina2, dias + 1, totalProducidas);
    }
}

int main(){
    cout << "Ingresa el tamaño del pedido: ";
    cin >> tamanioDelPedido;
    cout << "Ingresa la produccion diaria de la maquina 1: ";
    cin >> maquina1;
    cout << "Ingresa la produccion diaria de la maquina 2 (preferiblemente que la producción de ambas maquina sea diferente): ";
    cin >> maquina2;
    int resultado = calcularDias(maquina1, maquina2, dias);
    cout << "Se necesitan " << resultado << " días para completar el pedido." << endl;

    return 0;
}
