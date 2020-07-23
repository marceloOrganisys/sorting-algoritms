<?php
// simplest sorting algorithm
// algoritmo mais simples de ordenação

function getMin($array) {
    $minor = $array[0];

    foreach ($array as $n) {
        if ($n < $minor) {
            $minor = $n;
        }
    }
    return $minor;
}

$array1 = array(3, 5, 8, 9, 2, 5, 0, 4, 5);
$sortedArray = [];
echo ('<br>');
echo ('Normal -> ' . implode(',', $array1));

$count = 0;
$size = count($array1);

while ($count < $size) {
    $minor = getMin($array1);
    $sortedArray[] = $minor;
    foreach ($array1 as $key => $value) {
        if ($value == $minor) {
            array_splice($array1, $key, 1);
            // array_splice delete a index and reindexes the array
            // array_splice deleta o index definido e reseta os índices do array
            break;
        }
    }
    $count++;
}

echo ('<br>Sorted -> ' . implode(',', $sortedArray));

// The concept is to get the minor value and to move it to another array,   
// then you remove this value from the original array

// A ideia é encontrar o menor valor do array e movê-lo para outro array,
// depois o valor movido é removido do array original