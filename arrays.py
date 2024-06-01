# Largest element in an array

def find_max(nums):
    max_num = nums[0]
    for i in nums:
        if i> max_num:
            max_num = i
    return max_num

# Second largest

def second_largest(nums):
    ans = []
    max_num = nums[0]
    sec_max = nums[0]
    for i in nums:
        if i > max_num:
            sec_max = max_num
            max_num = i
        elif i < max_num & i > sec_max:
            sec_max = i
    ans.append(max_num)
    ans.append(sec_max)
    return ans

def getSecondOrderElement(arr, n):
    slargest = sLargest(arr,n)
    ssmallest = sSmallest(arr,n)

    return [slargest, ssmallest]

def sLargest(arr, n):
    max_num = -1
    sec_max = -1
    for i in arr:
        if i > max_num:
            sec_max = max_num
            max_num = i
        elif i > sec_max:
            sec_max = i
    return sec_max

def sSmallest(arr,n):
    smallest = float('inf')
    sec_min = float('inf')
    for i in arr:
        if i < smallest:
            sec_min = smallest
            smallest = i
        elif i < sec_min:
            sec_min = i
    return sec_min


# Check if sorted

def isSorted(n: int,  a: [int]) -> int:
    for i in range(1, n):
        if a[i] >= a[i-1]:
            pass
        else:
            return False
    return True

# Remove Duplicates from the sorted array
        # 1 2 3 3 4 5 6 7 7

def remove_duplicate(arr):
    i = 0  
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i += 1
    return print(arr)

# Left rotate by 1

# 1 2 3 4 5 
# 2 3 4 5 1

# 1 2 3 4 5 6 7 8 9
# 4 5 6 7 8 9 1 2 3 

def left_by_k(arr, k):
    n = len(arr)
    k = k % n

    for i in  range(k//2):
        arr[i],arr[k-1-i] = arr[k-1-i], arr[i]
    print(arr)
    for j in range((n-k)//2):
        arr[k+j], arr[n-1-j] = arr[n-1-j], arr[k+j]
    print(arr)
    for i in range(n//2):
        arr[i], arr[n-1-i] = arr[n-1-i] , arr[i]
    return arr

print(left_by_k([1,2,3,4,5,6,7,8,9],3))


def lefft_rotate(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[i] = temp
    return arr



# print(lefft_rotate([1,2,3,4,5]))



def left_rotate(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[i] = temp
    return arr

# def left_rotate(arr, k):

    k = k % len(arr)
    n = len(arr)
    temp = []

    for i in range(k):
        temp.append(arr[i])
        
    for j in range(n-k):
        arr[j] = arr[k+j]

    for i in range(k):
        arr[j+1] = temp[i]
        j += 1
    
    print(arr)


def left_rotates(arr, k):

    n = len(arr)
    k = k % n 

    for i in range(k//2):         
        temp = arr[i]
        arr[i] = arr[k-1-i]
        arr[k-1-i] = temp

    for j in range((n-k)//2):
        temp = arr[k+j]
        arr[k+j] = arr[n-1-j]
        arr[n-1-j] = temp

    for i in range(n//2):
        temp = arr[i]
        arr[i] = arr[n-1-i]
        arr[n-1-i] = temp
    
    return arr

def right_rotates(arr, k):

    n = len(arr)
    k = k % n
    temp = []

    for i in range(k):
        temp.append(arr[n-k+i])

    for i in range(n-1,-1,-1):
        arr[i] = arr[i-k]
        
    for i in range(k):
        arr[i] = temp[i]

    return arr

def right_rotates(arr, k):
    
    n = len(arr)
    k = k % n

    for i in range((n-k)//2):       
        temp = arr[i]
        arr[i] = arr[(n-k-1)-i]
        arr[(n-k-1)-i] = temp
    print(arr)

    for j in range(k//2):
        temp = arr[n-k+j]
        arr[n-k+j] = arr[n-1-j]
        arr[n-1-j] = temp
    print(arr)

    for i in range(n//2):
        temp = arr[i]
        arr[i] = arr[n-1-i]
        arr[n-1-i] = temp

    return arr

def reverse_arr(arr):

    temp = arr[0]
    n = len(arr)
    for i in range(n//2):
        temp = arr[i]
        arr[i] = arr[n-1-i]
        arr[n-1-i] = temp
    print(arr)
        
# 1 2 0 5 9 0 0 4 3
# 1 2 5 9 0 0 0 

def move_zero_toend(arr):

    n = len(arr)
    j = -1
    
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    
    if j == -1:
        return arr

    for i in range(j, n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
        
    return arr

# def union_arr(arr1, arr2):
#     n1 = len(arr1)
#     n2 = len(arr2)

#     union = []

#     i = 0
#     j = 0

#     while i < n1 and j < n2:
#         if arr1[i] <= arr2[j]:
#             if len(union) == 0 or union[i-1] != arr1[i]:
#                 union.append(arr1[i])
#             i += 1
#         elif arr2[j] < arr1[i]:
#             if len(union) == 0 or union[j-1] != arr2[j]:
#                 union.append(arr2[j])
#             j += 1


#     return union

def insection_arr(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    i = j = 0
    result = []

    while i < n1 and j < n2:
        if arr1[i] == arr2[j]:
                result.append(arr1[i])
                i += 1
                j += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            i+=1
    return result

def missingNumber(a , N : int) -> int:
    # Write your code here.
    for i in range(N-1):
        if a[i] != i+1:
            return i+1
    return i+2

arr1 = [1, 2, 3, 4, 5, 6, 7,8, 9, 10]
arr2 = [2, 5, 6, 7, 8, 8, 9]


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    j = -1
    n = len(nums)
    for i in range(n):
        if nums[i] == val:
            j = i
            break
    
    if j == -1:
        return n, nums

    for i in range(j, n):
        if nums[i] != val:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return j+1, nums
    
print(removeElement([0,1,2,2,3,0,4,2], 2))





    
        