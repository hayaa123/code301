
def merge_sort(arr):
    '''
    this functio takes arr as an input and return you the sorted array using merge sort algorithem 
    '''
    n= len(arr)

    if n > 1 :
        mid = n//2  
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)

        merge_sort(right)

        merge(left,right,arr)
        return arr
    else:
        return arr
def merge(left,right,arr):
    i=0
    j=0
    k=0 
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1

    if i == len(left):
        arr[k:] = right[j:]
    else:
        arr[k:] = left[i:]



