# List of transmission and mcode files
transmission_files = ["transmission01.txt", "transmission02.txt"]
mcode_files = ["mcode01.txt", "mcode02.txt", "mcode03.txt"]

def z_algorithm(string):
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
    n = len(string)
    suffix_array = [i for i in range(n)]
    suffix_array.sort(key=lambda i: string[i:])
    return suffix_array

def build_lcp(string, suffix_array):
    n = len(string)
    rank = [0] * n
    lcp = [0] * n
    h = 0

    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and string[i + h] == string[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp

def find_longest_palindrome(string):
    rev_string = string[::-1]
    combined = string + '$' + rev_string
    suffix_array = generate_suffix_array(combined)
    lcp = build_lcp(combined, suffix_array)

    max_len = 0
    start_pos = 0
    n = len(string)

    for i in range(1, len(combined)):
        suffix1 = suffix_array[i]
        suffix2 = suffix_array[i - 1]

        if (suffix1 < n and suffix2 >= n + 1) or (suffix2 < n and suffix1 >= n + 1):
            if lcp[i] > max_len:
                max_len = lcp[i]
                start_pos = min(suffix1, suffix2)

    return start_pos + 1, start_pos + max_len

def longest_common_substring(string1, string2):
    n, m = len(string1), len(string2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_pos = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i

    return end_pos - max_len + 1, end_pos

def m_analysis(transmission_files, mcode_files):
    transmission_files_content = [0] * len(transmission_files)

    for x in range(len(transmission_files)):
        with open(transmission_files[x], 'r') as transmission_file:
            transmission_files_content[x] = transmission_file.read().strip()
            print("\nArchivo analizado: " + transmission_files[x] + "\n")
            
            for mcode in mcode_files:
                print("Comparado contra: " + mcode + "\n")
                with open(mcode, 'r') as mcode_file:
                    mcode_content = mcode_file.read().strip()
             
                    combined_text = mcode_content + '$' + transmission_files_content[x]
                    z_array = z_algorithm(combined_text)
                    
                    m_code_found = False
                    for i in range(len(mcode_content) + 1, len(combined_text)):
                        if z_array[i] == len(mcode_content):
                            pos_inicial = i - len(mcode_content) - 1
                            pos_final = pos_inicial + len(mcode_content) - 1
                            print(f"[True] El código se encontró entre las posiciones: {pos_inicial + 1}, {pos_final + 1} \n")  # Ajuste a base 1
                            m_code_found = True
                    if not m_code_found:
                        print("[False] El código no se encontró en el archivo \n")

    for i, content in enumerate(transmission_files_content):
        start_pos, end_pos = find_longest_palindrome(content)
        print("\nCódigo espejeado (palíndromo) más grande encontrado en: " + transmission_files[i] + "\n")
        print(f"Palíndromo más largo en {transmission_files[i]}: {start_pos} {end_pos}\n")

    start_pos, end_pos = longest_common_substring(transmission_files_content[0], transmission_files_content[1])
    print(f"Substring común más largo entre transmission1.txt y transmission2.txt: {start_pos} {end_pos}")

m_analysis(transmission_files, mcode_files)
