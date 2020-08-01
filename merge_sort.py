import numpy as np
# O(n logn)
# a lot faster

array1 = [2, 4, 1, 6, 8, 5, 3, 7, 12]
# break in two halves -> l and r

# TAKES TWO SORTED ARRAYS AND MERGE THEM INTO ONE SORTED ARRAY
def merge(left, right): # left, right, array
    nL = len(left) # n of elements in l
    nR = len(right) # n of elements in r
    
    arr = np.zeros(nL + nR)
    i = 0 # smallest unpicked in l
    j = 0 # smallest unpicked in r
    k = 0 # index of position in a
    
    while i < nL and j < nR:
        if left[i] <= right[j]: # compare wich one is smaller
            arr[k] = left[i] # put it in the original array
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1 # increment position on original array        
        
    while i < nL: # in case there are leftovers in l
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < nR: # in case there are leftovers in r
        arr[k] = right[j]
        j += 1
        k += 1
        
    return arr

def merge_sort(a):
    size = len(a)
    if size <= 1:
        return a

    half = size // 2
            
    left = merge_sort(a[:half])
    right = merge_sort(a[half:])
    
    return merge(left, right)
    
    
print(merge_sort(array1))
