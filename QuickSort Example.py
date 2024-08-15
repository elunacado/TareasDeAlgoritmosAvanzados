# Serial numbers of the electronics that need sorting
serialNumbers = [
    1004, 2345, 1763, 982, 4567, 2231, 3451, 1902, 4321, 876, 
    3498, 1205, 998, 2845, 1672, 2348, 4120, 3912, 572, 1920, 
    760, 1307, 5843, 678, 4320, 2751, 923, 3647, 890, 2476
]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    
    middle = [x for x in arr if x == pivot]
    
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

sortedSerialNumbers = quicksort(serialNumbers)

print("Original Sorting Of The Serial Numbers (new products included):")
print(serialNumbers)
print("\nSorted Serial Numbers:")
print(sortedSerialNumbers)
