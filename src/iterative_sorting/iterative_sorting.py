# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range( i +1, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x

        if smallest_index is not i:
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
             
    return arr



print(selection_sort([7,2,9,4,7,1,0,8,3,6]))



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]


    return arr

print(bubble_sort([7,2,9,4,7,1,0,8,3,6]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr