// simplest sorting algorithm
// algoritmo mais simples de ordenação

getMin = array => {
    minor = array[0]

    array.forEach(element => {
        if (element < minor) {
            minor = element
        }    
    });

    return minor
}

array1 = [3, 5, 8, 9, 2, 5, 0, 4, 5]
sortedArray = []
size = array1.length
count = 0
console.log('Normal -> ' + array1)

while (count < size) {
    minor = getMin(array1)
    sortedArray.push(minor)
    index = array1.indexOf(minor)
    array1.splice(index, 1)
    count++
}
 
console.log('Sorted -> ' + sortedArray)

// the concept is to get the minor value and to move it to another array,
// then you remove this value from the original array

// a ideia é encontrar o menor valor do array e movê-lo para outro array,
// depois o valor movido é removido do array original