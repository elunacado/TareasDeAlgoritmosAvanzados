# Lista de archivos de transmisión y códigos "mcode"
transmission_files = ["transmission01.txt", "transmission02.txt"]
mcode_files = ["mcode01.txt", "mcode02.txt", "mcode03.txt"]

# Implementación del algoritmo Z que encuentra patrones en cadenas.
def z_algorithm(string):
    # Array Z que contiene la longitud de los prefijos más largos que coinciden con el substring inicial
    z_array = [0] * len(string)  
    l, r = 0, 0  # Inicializamos los límites izquierdo y derecho de la ventana [l, r]

    for i in range(1, len(string)):  # Recorremos la cadena desde el segundo carácter
        if i > r:  # Si el índice actual está fuera de la ventana, recalculamos la ventana
            l, r = i, i
            # Expandimos la ventana si coinciden caracteres
            while r < len(string) and string[r] == string[r - l]:
                r += 1
            z_array[i] = r - l  # Guardamos la longitud del prefijo coincidente
            r -= 1  # Reducimos el índice derecho para la próxima iteración
        else:
            k = i - l
            # Usamos un valor previamente calculado
            if z_array[k] < r - i + 1:
                z_array[i] = z_array[k]
            else:
                # Expandimos nuevamente la ventana en caso necesario
                l = i
                while r < len(string) and string[r] == string[r - l]:
                    r += 1
                z_array[i] = r - l
                r -= 1
    return z_array  # Devolvemos el array Z con los prefijos más largos

# Genera el array de sufijos de una cadena, que es un array de índices ordenados según los sufijos de la cadena
def generate_suffix_array(string):
    n = len(string)
    suffix_array = [i for i in range(n)]  # Array de sufijos inicializado con los índices
    suffix_array.sort(key=lambda i: string[i:])  # Ordenamos los sufijos según su valor
    return suffix_array  # Devolvemos el array de sufijos ordenado

# Construcción del array LCP (Longest Common Prefix), que guarda la longitud del prefijo más largo compartido entre sufijos adyacentes
def build_lcp(string, suffix_array):
    n = len(string)
    rank = [0] * n  # Array que almacena las posiciones de los sufijos
    lcp = [0] * n   # Array que almacena los valores LCP (Prefijos comunes más largos)
    h = 0  # Variable auxiliar para el cálculo de LCP

    # Rellenamos el array de posiciones de los sufijos en el array de sufijos
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i  
    
    # Calculamos el array LCP
    for i in range(n):
        if rank[i] > 0:  # Si no estamos en el primer sufijo
            j = suffix_array[rank[i] - 1]  # Obtenemos el sufijo anterior en el array
            # Comparamos caracteres para encontrar el prefijo común más largo
            while i + h < n and j + h < n and string[i + h] == string[j + h]:
                h += 1
            lcp[rank[i]] = h  # Guardamos la longitud del prefijo común más largo
            if h > 0:
                h -= 1  # Reducimos la longitud para la siguiente comparación
    return lcp  # Devolvemos el array LCP

# Encuentra el palíndromo más largo dentro de una cadena
def find_longest_palindrome(string):
    rev_string = string[::-1]  # Obtenemos la cadena invertida
    combined = string + '$' + rev_string  # Combinamos la cadena original con la invertida separada por un símbolo especial
    suffix_array = generate_suffix_array(combined)  # Generamos el array de sufijos
    lcp = build_lcp(combined, suffix_array)  # Construimos el array LCP

    max_len = 0  # Variable para almacenar la longitud máxima del palíndromo encontrado
    start_pos = 0  # Variable para almacenar la posición de inicio del palíndromo
    n = len(string)

    # Buscamos en el LCP el palíndromo más largo (cadena igual en ambas direcciones)
    for i in range(1, len(combined)):
        suffix1 = suffix_array[i]  # Primer sufijo
        suffix2 = suffix_array[i - 1]  # Segundo sufijo

        # Comprobamos si estamos comparando sufijos de la cadena original con la invertida
        if (suffix1 < n and suffix2 >= n + 1) or (suffix2 < n and suffix1 >= n + 1):
            if lcp[i] > max_len:  # Si encontramos un prefijo común más largo que el máximo
                max_len = lcp[i]  # Actualizamos la longitud máxima
                start_pos = min(suffix1, suffix2)  # Actualizamos la posición inicial

    return start_pos + 1, start_pos + max_len  # Devolvemos la posición del palíndromo y su longitud

# Encuentra la subcadena común más larga entre dos cadenas usando programación dinámica
def longest_common_substring(string1, string2):
    n, m = len(string1), len(string2)  # Longitud de ambas cadenas
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # Matriz de programación dinámica
    max_len = 0  # Longitud máxima de la subcadena común
    end_pos = 0  # Posición final de la subcadena común más larga

    # Llenamos la matriz DP
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:  # Si los caracteres coinciden
                dp[i][j] = dp[i - 1][j - 1] + 1  # Aumentamos el valor de la subcadena común
                if dp[i][j] > max_len:  # Actualizamos la longitud máxima si encontramos una subcadena más larga
                    max_len = dp[i][j]
                    end_pos = i

    return end_pos - max_len + 1, end_pos  # Devolvemos la posición inicial y final de la subcadena más larga

# Función principal que analiza los archivos de transmisión y códigos mcode
def m_analysis(transmission_files, mcode_files):
    # Array para almacenar el contenido de los archivos de transmisión
    transmission_files_content = [0] * len(transmission_files)

    # Leemos los archivos de transmisión
    for x in range(len(transmission_files)):
        with open(transmission_files[x], 'r') as transmission_file:
            transmission_files_content[x] = transmission_file.read().strip()  # Leemos el archivo y eliminamos espacios en blanco
            print("\nArchivo analizado: " + transmission_files[x] + "\n")
            
            # Comparación con los archivos mcode
            for mcode in mcode_files:
                print("Comparado contra: " + mcode + "\n")
                with open(mcode, 'r') as mcode_file:
                    mcode_content = mcode_file.read().strip()  # Leemos el archivo mcode y eliminamos espacios en blanco
             
                    # Combinamos el mcode con la transmisión para aplicar el algoritmo Z
                    combined_text = mcode_content + '$' + transmission_files_content[x]
                    z_array = z_algorithm(combined_text)  # Aplicamos el algoritmo Z
                    
                    m_code_found = False  # Bandera para saber si se encontró el mcode
                    # Buscamos el mcode en la transmisión
                    for i in range(len(mcode_content) + 1, len(combined_text)):
                        if z_array[i] == len(mcode_content):  # Si encontramos una coincidencia completa
                            pos_inicial = i - len(mcode_content) - 1  # Calculamos la posición inicial
                            pos_final = pos_inicial + len(mcode_content) - 1  # Calculamos la posición final
                            print(f"[True] El código se encontró entre las posiciones: {pos_inicial + 1}, {pos_final + 1} \n")  # Ajuste a base 1
                            m_code_found = True
                    if not m_code_found:  # Si no se encontró el mcode
                        print("[False] El código no se encontró en el archivo \n")

    # Buscamos el palíndromo más largo en cada archivo de transmisión
    for i, content in enumerate(transmission_files_content):
        start_pos, end_pos = find_longest_palindrome(content)  # Llamamos a la función para encontrar el palíndromo más largo
        print("\nCódigo espejeado (palíndromo) más grande encontrado en: " + transmission_files[i] + "\n")
        print(f"Palíndromo más largo en {transmission_files[i]}: {start_pos} {end_pos}\n")

    # Buscamos la subcadena común más larga entre los dos archivos de transmisión
    start_pos, end_pos = longest_common_substring(transmission_files_content[0], transmission_files_content[1])
    
    # Imprimimos la posición inicial y final de la subcadena común más larga encontrada
    print(f"Substring común más largo entre transmission1.txt y transmission2.txt: {start_pos} {end_pos}")

# Llamamos a la función principal 'm_analysis' para analizar los archivos de transmisión y comparar con los archivos mcode
m_analysis(transmission_files, mcode_files)
