
transmissionFiles = ["transmission01.txt","transmission02.txt"]
mcodeFiles = ["mcode01.txt","mcode02.txt","mcode03.txt"]

def zAlgorithm(string):
    zArray = [0] * len(string)

    l, r = 0, 0

    for i in range(1, len(string)):
        if i > r:
            l, r = i, i
            while r < len(string) and string[r] == string[r - l]:
                r += 1
            zArray[i] = r - l
            r -= 1
        else:
            k = i - l
            if zArray[k] < r - i + 1:
                zArray[i] = zArray[k]
            else:
                l = i
                while r < len(string) and string[r] == string[r - l]:
                    r += 1
                zArray[i] = r - l
                r -= 1
    return zArray

def generateSuffixArray(string):
    n = len(string)
    suffix_array = [i for i in range(n)]
    suffix_array.sort(key=lambda i: string[i:])
    return suffix_array

def findLongestPalindrome(string):
    pass

def mAnalysis(transmissionFiles, mcodeFiles):

    transmissionFilesContent = [0] * len(transmissionFiles)

    for x in range(len(transmissionFiles)):
        mCodeFound = False
        with open(transmissionFiles[x], 'r') as tF:
            transmissionFilesContent[x] = tF.read()
            print("\nArchivo analizado: " + transmissionFiles[x] + "\n")
            
            for m in mcodeFiles:
                print("Comparado contra: " + m + "\n")
                with open(m, 'r') as mF:
                    mcodeContent = mF.read()
                    
                    # Combine the pattern and string to pass it to the Z Algorithm function
                    combinedText = mcodeContent + '$' + transmissionFilesContent[x]
                    
                    zArray = zAlgorithm(combinedText)
                    
                    for i in range(combinedText.find("$") + 1, len(combinedText)):
                        if zArray[i] == len(mcodeContent):
                            pos = i - (len(mcodeContent) + 1)
                            mCodeFound = True
                            print(f"[True] El código se encontró entre las siguientes posiciones: {pos}, {pos + len(mcodeContent) - 1} \n")
                    if(mCodeFound != True):
                        print("[False] El código no se encontró en el archivo \n")

    for i, content in enumerate(transmissionFilesContent):
        # startPos, finalPos = findLongestPalindrome(content)
        print("\nCódigo espejeado (palíndromo) más grande encontrado en: " + transmissionFiles[i] + "\n")
        # print(f"Posición Inicial: {startPos} Posición Final: {finalPos}\n")




        
mAnalysis(transmissionFiles, mcodeFiles)
