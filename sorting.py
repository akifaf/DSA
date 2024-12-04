arr = [88, 33, 22, 77, 55, 99, 11, 44, 66]

def bubble_sort(arr):
    n = len(arr)

    for j in range(n-1):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    print(arr)

def selection_sort(arr):

    min = 0
    n = len(arr)
    
    for i in range(n-1):
        min = i
        for j in range(i, n):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[min], arr[i] = arr[i], arr[min]

arr = [88, 33, 22, 77, 55, 99, 11, 44, 66]

def insertion_sort(arr):
    
    n = len(arr)

    for i in range(n-1):
        j = i + 1
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr

# insertion_sort(arr)
print(arr)

# def merge_sort(arr):

#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_arr = arr[:mid]
#         right_arr = arr[mid:]

#         merge_sort(left_arr)
#         merge_sort(right_arr)

#         i = j = k = 0

#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr[i] < right_arr[j]:
#                 arr[k] = left_arr[i]
#                 i += 1
#                 k += 1
#             else:
#                 arr[k] = right_arr[j]
#                 j += 1
#                 k += 1
        
#         while i < len(left_arr):
#             arr[k] = left_arr[i]
#             i += 1
#             k += 1
#         while j < len(right_arr):
#             arr[k] = right_arr[j]
#             j += 1
#             k += 1

def quick_sort(arr, left, right):

    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos-1)
        quick_sort(arr, partition_pos+1, right)

    

def partition(arr, left, right):

    pivot = arr[right]
    i = left
    j = right -1

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j and arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]    


def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):

            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(left_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
merge_sort(arr)
print(arr)
