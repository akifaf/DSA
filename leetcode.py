# # nums = [4,1,2,1,2]

# # dict = {}

# # for i in nums:
# #     dict[i] = dict.get(i, 0) + 1

# # for i in dict:
# #     if dict[i] == 1:
# #         print(i)


# # generate subarray


# nums = [1,2,3]
# subarray = []
# arr = []

# for i in range(len(nums)):
#     for j in range(i, len(nums)):
#         arr.append(nums[j])
#     subarray.append(arr)
#     arr = []
# print(subarray)


arr = [2,4,6,7,8,22,54,77,78,89,99]
# k = 100

# def binary_search(arr, low, high):
#     if low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == k :
#             print(mid)
#             return mid
#         if k < arr[mid]:
#             binary_search(arr, low, mid-1)
#         else:
#             binary_search(arr, mid+1, high)
#     else:
#         print(-1)
        
# binary_search(arr, 0, len(arr)-1)
arr = [2,4,6,7,8,81, 98]
def bn(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid
        elif k < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1

print(bn(arr, 98))