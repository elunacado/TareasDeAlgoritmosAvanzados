numOfDenominations = int(input("Enter the amount of denominations: "))

def countChange(numOfDenominations):
    denominations = []
    timesUsed = []

    for x in range(numOfDenominations):
        denominationNum = int(input("Enter the denomination number: "))
        denominations.append(denominationNum)

    denominations.sort(reverse=True)

    for x in range(len(denominations)):
        timesUsed.append(0)
        
    productPrice = int(input("Product Price: "))
    payAmount = int(input("Payed Amount: "))

    change = payAmount - productPrice

    counter = 0

    i = 0
    while counter < change and i < len(denominations):
        if counter + denominations[i] <= change:
            counter += denominations[i]
            timesUsed[i] += 1
        else:
            i += 1

    if counter == change:
        return timesUsed
    else:
        print("Exact change can't be given")
        return 

result = countChange(numOfDenominations)
if result:
    print(result)