def insertion_sort(arr):
    '''
    this function is ment to sort the array in insertion sort algorithm 
    it takes arr as input and return sorted array
    '''
    for index,value in enumerate(arr):
        j = index -1 
        temp = value

        while j>=0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = temp
    return arr