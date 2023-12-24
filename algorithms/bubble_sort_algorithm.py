def bubble_sort_algorithm(arr):
    """
    bubble sort
    """
    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    return arr


arr = [1,12,9,2,3,52,13]
print(bubble_sort_algorithm(arr))