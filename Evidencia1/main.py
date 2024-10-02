# List of transmission and mcode files
transmission_files = ["transmission01.txt", "transmission02.txt"]
mcode_files = ["mcode01.txt", "mcode02.txt", "mcode03.txt"]

def z_algorithm(string):
    """
    Implementación del algoritmo Z para buscar coincidencias.
    """
    z_array = [0] * len(string)
    l, r = 0, 0

    for i in range(1, len(string)):
        if i > r:
            l, r = i, i
            while r < len(string) and string[r] == string[r - l]:
                r += 1
            z_array[i] = r - l
            r -= 1
        else:
            k = i - l
            if z_array[k] < r - i + 1:
                z_array[i] = z_array[k]
            else:
                l = i
                while r < len(string) and string[r] == string[r - l]:
                    r += 1
                z_array[i] = r - l
                r -= 1
    return z_array

def generate_suffix_array(string):
    """
    Genera el arreglo de sufijos de un string dado.
    """
    n = len(string)
    suffix_array = [i for i in range(n)]
    suffix_array.sort(key=lambda i: string[i:])
    return suffix_array

def find_longest_palindrome(string):
    """
    Encuentra el palíndromo más largo en un string.
    """
    pass

def m_analysis(transmission_files, mcode_files):
    """
    Realiza el análisis de los archivos de transmisión contra los códigos M.
    """
    transmission_files_content = [0] * len(transmission_files)

    for x in range(len(transmission_files)):
        m_code_found = False
        with open(transmission_files[x], 'r') as transmission_file:
            transmission_files_content[x] = transmission_file.read()
            print("\nArchivo analizado: " + transmission_files[x] + "\n")
            
            for mcode in mcode_files:
                print("Comparado contra: " + mcode + "\n")
                with open(mcode, 'r') as mcode_file:
                    mcode_content = mcode_file.read()
                    
                    # Combina el patrón y el string para pasarlo a la función del algoritmo Z
                    combined_text = mcode_content + '$' + transmission_files_content[x]
                    
                    z_array = z_algorithm(combined_text)
                    
                    for i in range(combined_text.find("$") + 1, len(combined_text)):
                        if z_array[i] == len(mcode_content):
                            pos = i - (len(mcode_content) + 1)
                            m_code_found = True
                            print(f"[True] El código se encontró entre las siguientes posiciones: {pos}, {pos + len(mcode_content) - 1} \n")
                    if not m_code_found:
                        print("[False] El código no se encontró en el archivo \n")

    for i, content in enumerate(transmission_files_content):
        # start_pos, final_pos = find_longest_palindrome(content)
        print("\nCódigo espejeado (palíndromo) más grande encontrado en: " + transmission_files[i] + "\n")
        # print(f"Posición Inicial: {start_pos} Posición Final: {final_pos}\n")

# Ejecuta el análisis con los archivos de transmisión y los códigos M
m_analysis(transmission_files, mcode_files)
