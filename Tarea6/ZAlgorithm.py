def zAlgorithm(string):

    zMatrix = [0] * len(string)

    for i in range(len(string)):
        r = i
        while r < len(string) and string[r - i] == string[r]:
            r += 1
        
        zMatrix[i] = r - i

    return zMatrix

string = input("Enter the string you want to analyze: ")

print(zAlgorithm(string))
