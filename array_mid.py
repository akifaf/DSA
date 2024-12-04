# find the maximum sum of the subarray

arr = [1,2,3]

def maxSum(arr):
    result = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            result = max(sum, result)
    print(result)


# Kadane's alg

arr = [-2,1,-3,4,-1,2,1,-5,4]

def maxSumOfSubarray(arr):

    maximum = float('-inf')
    sum = 0

    for i in range(len(arr)):
        sum += arr[i]
        if sum > maximum:
            maximum = sum
        if sum < 0:
            sum = 0

    return print(maximum)

arr = [-2,-1,4,-2,5]

def maxSumSubarray(arr):

    start = end = 0
    maximum = float('-inf')
    sum = 0

    for k in range(len(arr)):
        sum += arr[k]
        if sum > maximum:
            maximum = sum
            end = k
        if sum < 0:
            sum = 0
            if k+1 <= len(arr)-1:
                start = k+1
            else:
                start = k

    print(arr[start:end+1])

# maxSumSubarray(arr)

# maxSumOfSubarray(arr)

arr =  [3,1,-2,-5,2,-4]

def rearrangeArray(arr):
    pos = []
    neg = []
    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    
    i = j = k = 0
    
    for i in range(len(arr)//2):
        arr[2*i] = pos[i]
        arr[2*i + 1] = neg[i]

    return print(arr)

arr =  [3,1,-2,-5,2,-4]
rearrangeArray(arr)

def rearrangeArr(arr):

    i = j = 0

    while i < len(arr):
        pass