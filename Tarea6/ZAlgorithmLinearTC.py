# Based on GeekForGeeks Code and ChatGPT explanation
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

string = input("Enter the string you want to analyze: ")

print(zAlgorithm(string))
