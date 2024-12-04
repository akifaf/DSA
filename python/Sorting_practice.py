def selection_sort(arr):

    for i in range(len(arr)):
        maxi = i
        for j in range(i, len(arr)):
            if arr[j] > arr[maxi]:
                maxi = j
        arr[i], arr[maxi] = arr[maxi], arr[i]

    return print(arr)

arr = [22, 11, 88, 66, 55, 77, 33, 44]

# selection_sort(arr)

def bubble_sort(arr):

    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)

    print(arr)

bubble_sort(arr)