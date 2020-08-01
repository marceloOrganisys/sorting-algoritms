# always moves a bigger to the top 

array1 = [2, 7, 4, 1, 5, 3]
array2 = [3, 5, 8, 9, 2, 5, 0, 4, 5]

def bubleSort(array):
    repeat = len(array) - 1
    while repeat >= 1:
        flag = 0
        for i in range(0, repeat):
            if array[i] > array[i+1]:
                # invertion without new variable
                array[i] += array[i+1]
                array[i+1] = array[i] - array[i+1]
                array[i] -= array[i+1]
                flag = 1
                
        # in case there no swaps (array already sorted)]
        # if the input is a sorted array, there will be only 1 execution
        if flag == 0:
            break
        
        repeat -= 1
    return array
        
print(bubleSort(array1))
print(bubleSort(array2))

# time
    # best-case: O(n)
    # worst-case: O(n²)
    
# sort algorith is slow