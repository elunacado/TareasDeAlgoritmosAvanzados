def zAlgorithm(pattern, text):
    patternLength = len(pattern)
    textLength = len(text)

    zArray = [0] * textLength
    
    for i in range(textLength):
        matchLength = 0

        while (i + matchLength < textLength) and (matchLength < patternLength) and (text[i + matchLength] == pattern[matchLength]):
            matchLength += 1
            
        # Guardar cuántos caracteres coinciden desde la posición i
        zArray[i] = matchLength

    return zArray


pattern = "10010001"
text = "000100100100010111"

#pattern = "aab"
#text = "baabaa"

print(zAlgorithm(pattern, text))