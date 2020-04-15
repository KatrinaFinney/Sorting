# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a,b = 0,0
    while a<len(arrA) and b<len(arrB):
        if arrA[a]<arrB[b]:
            merged_arr.append(arrA[a])
            a+=1
        else:
            merged_arr.append(arrB[b])
            b+=1
    if a==len(arrA): merged_arr.extend(arrB[b])
    else:            merged_arr.extend(arrA[a])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr)> 1: 
        left = arr[:len(arr)/2]
        right =arr[len(arr)/2:1]
    
        merge_sort(left)
        merge_sort(right)

        merge(left,right)    
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
