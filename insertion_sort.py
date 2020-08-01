# little more efficient than buble and selection sort

array1 = [2, 7, 4, 1, 5, 3]

def insertionSort(array):
    for i in range(1, len(array)):
        current = i
        value = array[i]
        while (current > 0 and array[current - 1] > value):
            array[current] = array[current - 1]
            current -= 1
            
        array[current] = value
        
    return array

print(insertionSort(array1))
            

