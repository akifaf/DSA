
def binary_search(arr, value):

    low , high = 0, len(arr)-1

    while low <= high:

        mid = (low + high) // 2

        if value == arr[mid]:
            return mid
        
        elif value < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def searchh(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        
        mid = (low + high) // 2

        if target == arr[mid]:
            return mid
        
        elif target < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    else:
        return -1

def search_rec(arr, target, low, high):

    if low > high :
        return -1
    
    mid = (low + high) // 2

    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return search_rec(arr, target, low, mid-1)
    else:
        return search_rec(arr, target, mid+1, high)


# print(search_rec([1,2,3,5,5,6,7,8,9], 4, 0, 8))

def lower_bound(arr, value):
    ans = len(arr)
    low, high = 0, len(arr) -1

    while low <= high:

        mid = (low + high) // 2

        if value <=  arr[mid]:
            ans = mid
            high = mid - 1
        elif value > arr[mid]:
            ans = mid + 1
            low = mid + 1
        
    return ans
# print(lower_bound([1,1,3,4,4,8,9,9,9,10], 2))

def upper_bound(arr, value):

    low, high = 0, len(arr)-1

    pos = len(arr)

    while low < high:

        if low == high:
            return pos

        mid = (low + high) // 2

        if value >= arr[mid]:
            pos = mid
            low = mid + 1 
        else:
            pos = mid -1
            high = mid-1

    return pos

arr = [1,1,3,4,4,8,9,9,9,10]

print(lower_bound(arr, 9))
























