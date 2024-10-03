#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <sstream>

void imprimirTabla(const std::vector<std::string>& tabla) {
    std::cout << "Tabla generada:\n";
    for (const auto& fila : tabla) {
        std::cout << fila << std::endl;
    }
}

std::string toHex(int num) {
    std::stringstream ss;
    ss << std::uppercase << std::setw(2) << std::setfill('0') << std::hex << num;
    return ss.str();
}

int main() {
    std::string nombreArchivo;
    int n;

    // Leer el nombre del archivo y el valor de n
    std::cout << "Introduce el nombre del archivo (datos.txt): ";
    std::cin >> nombreArchivo;
    std::cout << "Introduce un entero n (múltiplo de 4 y entre 16 y 64): ";
    std::cin >> n;

    // Validar que n sea múltiplo de 4 y esté en el rango adecuado
    if (n % 4 != 0 || n < 16 || n > 64) {
        std::cerr << "Error: n debe ser un múltiplo de 4 y estar entre 16 y 64." << std::endl;
        return 1;
    }

    std::ifstream archivo(nombreArchivo);
    if (!archivo) {
        std::cerr << "Error al abrir el archivo." << std::endl;
        return 1;
    }

    std::vector<char> caracteres;
    char c;
    // Leer todos los caracteres del archivo
    while (archivo.get(c)) {
        if (c == '\n') {
            caracteres.push_back('-'); // Reemplazar salto de línea por '-'
        } else {
            caracteres.push_back(c);
        }
    }
    archivo.close();

    // Crear la tabla
    int filas = (caracteres.size() + n - 1) / n; // Número de filas necesarias
    std::vector<std::string> tabla(filas, std::string(n, ']')); // Inicializar con ']'

    // Llenar la tabla
    for (int i = 0; i < caracteres.size(); ++i) {
        tabla[i / n][i % n] = caracteres[i];
    }

    // Imprimir la tabla
    imprimirTabla(tabla);

    // Calcular el arreglo a
    std::vector<int> a(n, 0);
    for (int col = 0; col < n; ++col) {
        for (int fila = 0; fila < filas; ++fila) {
            if (fila * n + col < caracteres.size()) { // Evitar overflow
                a[col] += static_cast<int>(tabla[fila][col]);
            }
        }
        a[col] %= 256; // Aplicar la operación módulo
    }

    // Generar la cadena de salida en hexadecimal
    std::string salida;
    for (int i = 0; i < n; i += 4) {
        salida += toHex(a[i]);
    }

    // Mostrar el arreglo a y la cadena de salida
    std::cout << "Arreglo a: ";
    for (const auto& valor : a) {
        std::cout << valor << " ";
    }
    std::cout << std::endl;

    std::cout << "Cadena de salida: " << salida << std::endl;

    return 0;
}
