# simplest sorting algorithm
# algoritmo mais simples de ordenação

def getMin(array):
    minor = array[0]
    
    for n in array:
        if n < minor:
            minor = n
    
    return minor

array1 = [3, 5, 8, 9, 2, 5, 0, 4, 5]
sortedArray = []
print('\n')
print('Normal -> ', array1)

count = 0
size = len(array1)

while count < size:
    minor = getMin(array1)
    sortedArray.append(minor)
    array1.remove(minor)
    count += 1
    
print('Sorted -> ', sortedArray)

# the concept is to get the minor value and to move it to another array
# then you remove this value from the original array

# a ideia é encontrar o menor valor do array e movê-lo para outro array
# depois o valor movido é removido do array original