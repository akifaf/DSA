# arr = [5,2,8,9,7,1]              
                                
# for i in range(len(arr)):        
#     min = i                         
#     for j in range(i+1, len(arr)):  
#         if arr[j] < arr[min]:       
#             min = j                 
#     arr[min], arr[i] = arr[i], arr[min] 

# # print(arr)                             

# arr = [
#     {'First Name': 'Raj', 'Last Name': 'Nayyar'},
#     {'First Name': 'Suraj', 'Last Name': 'Sharma'},
#     {'First Name': 'Karan', 'Last Name': 'Kumar'},
#     {'First Name': 'Jade', 'Last Name': 'Canary'},
#     {'First Name': 'Raj', 'Last Name': 'Thakur'},
#     {'First Name': 'Raj', 'Last Name': 'Sharma'},
#     {'First Name': 'Kiran', 'Last Name': 'Kamla'},
#     {'First Name': 'Armaan', 'Last Name': 'Kumar'},
#     {'First Name': 'Jaya', 'Last Name': 'Sharma'},
#     {'First Name': 'Ingrid', 'Last Name': 'Galore'},
#     {'First Name': 'Jaya', 'Last Name': 'Seth'},
#     {'First Name': 'Armaan', 'Last Name': 'Dadra'},
#     {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
#     {'First Name': 'Aahana', 'Last Name': 'Arora'}
# ]

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j]['First Name'][0] < arr[min_index]['First Name'][0]:
#                 min_index = j
#         if min_index != i:
#             arr[i], arr[min_index] = arr[min_index], arr[i]
    
#     return print(arr)


# # print(selection_sort(arr))


# def sort(nums, target):
#         n = len(nums)
#         target_index = []
#         for i in range(n):
#             min_index = i
#             for j in range(i+1, n):
#                 if nums[j] < nums[min_index]:
#                     min_index = j
#             if min_index != i:
#                 nums[i], nums[min_index] = nums[min_index], nums[i]
#             if nums[i] == target:
#                 target_index.append(i)

#         return target_index



# print(sort([1,2,5,2,3], 2))

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr
    
# # print(bubble_sort([5,4,7,2,1,3]))

# arr = [22, 11, 88, 66, 55, 77, 33, 44]

# def quicksort(arr, left, right):
#     if left < right:
#         partition_pos = partition(arr, left, right)
#         quicksort(arr, left, partition_pos-1)
#         quicksort(arr, partition_pos+1, right)

#     return arr

# def partition(arr, left, right):
#     i = left
#     j = right-1
#     pivot = arr[right]

#     while i < j:

#         while arr[i] < pivot and i < right:
#             i += 1

#         while arr[j] >= pivot and j > left:
#             j -= 1

#         if i < j:
#             print('i', i , 'arr[i] = ', arr[i], arr[j])
#             arr[i], arr[j] = arr[j], arr[i]

#     if arr[i] > pivot:
#         arr[i], arr[right] = arr[right], arr[i]

#     return i

# # print(quicksort(arr, 0, len(arr)-1))

# arr = [22, 11, 88, 66, 55, 44, 33, 44]

# def quicksort(arr, left, right):
#     if left < right:
#         partion_pos = partition(arr, left, right)
#         quicksort(arr, left, partion_pos-1)
#         quicksort(arr, partion_pos+1, right)

# def partition(arr, left, right):
#     i = left
#     j = right-1
#     pivot = arr[right]

#     while i < j:
#         while arr[i] > pivot and i < right:
#             i += 1
#         while arr[j] <= pivot and j > left:
#             j -= 1
#         if i < j :
#             arr[i], arr[j] = arr[j], arr[i]
#     if  arr[i] < pivot:
#         arr[i], arr[right] = arr[right], arr[i]

#     return i

# # quicksort(arr, 0, len(arr)-1)
# # print(arr)



# arr = [2,6,5,1,3,4]

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while arr[j-1] > arr[j] and j > 0:
#             arr[j-1] , arr[j] = arr[j] , arr[j-1]
#             j -= 1
        


# arr = [2,6,5,1,3,4]

# def insertion_sorting(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while j > 0 and arr[j-1] < arr[j]:
#             arr[j-1], arr[j] = arr[j], arr[j-1]
#             j -= 1

# # insertion_sorting(arr)

# # print(arr)
            


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i 
#         while j > 0 and arr[j-1] > arr[j]:
#             arr[j-1], arr[j] = arr[j], arr[j-1]
#             j -= 1    

# arr = [22, 11, 88, 66, 55, 77, 33, 44]

# def quick_sort(arr, left, right):

#     if left < right:
#         partition_pos = partition(arr, left, right)
#         quick_sort(arr, left, partition_pos-1)
#         quick_sort(arr, partition_pos+1, right)

# def partition(arr, left, right):
#     pivot = arr[right]
#     i = left
#     j = right - 1

#     while i < j:

#         while arr[i] < pivot and i < right:
#             i += 1
#         while arr[j] >= pivot and j > left:
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
        
#     if arr[i] > pivot:
#         arr[i], arr[right] = arr[right], arr[i]

#     return i    

# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[min_index] > arr[j]:
#                 min_index = j
#         if min_index != i:
#             arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# # arr = [2,6,5,1,3,3]

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]


# quick_sort(arr, 0, len(arr)-1)
# print(arr)




def selection_sort(arr):
    
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
        
    return print(arr)

arr = [22, 11, 88, 66, 55, 77, 33, 44]

def bubble_sort(arr):
    
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i 
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1] , arr[j]
            j -= 1
           
    print(arr)


def quick_sort(arr, left, right):
    
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos-1)
        quick_sort(arr, partition_pos+1, right)


def partition(arr, left, right):

    pivot = arr[right]
    i = left
    j = right-1

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j and arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i 

arr = [22, 11, 88, 66, 55,11, 77, 33, 44, 88]

# quick_sort(arr, 0, len(arr)-1)
# print(arr)
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
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

 
# merge_sort(arr)
# print(arr)











def quick(arr, left, right):

    if left < right:
        partition_pos = partition(arr, left, right)
        quick(arr, left, partition_pos-1)
        quick(arr, partition_pos+1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    j = right - 1

    while i< j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j and arr[i] > arr[j] :
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

quick(arr, 0  , len(arr)-1)

print(arr)
