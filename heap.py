arr = [3, 5,2, 64,12,62,65,12,33]
arr = [3, 6, 5, 0, 8, 2, 1, 9]

def max_heapify(arr, i, x):
    n = x - 1
    L = 2 * i + 1
    R = 2 * i + 2
    largest = i
    if L <= n and arr[L] > arr[i]:
        largest = L
    if R <= n and arr[R] > arr[largest]:
        largest = R
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)


def build_max_heap(arr):
    n = len(arr)
    i = (n//2) - 1
    while i>=0:
        max_heapify(arr, i)
        i -= 1

# build_max_heap(arr)

def build_heap(arr):
    n = len(arr)
    i = (n//2) -1
    while i >= 0:
        max_heapify(arr, i)
        i -= 1

# build_heap(arr)

def insert(arr, value):
    arr.append(value)
    n = len(arr)
    i = (n//2) - 1
    while i >= 0:
        max_heapify(arr, i)
        i-= 1
    print(arr)

# insert(arr, 33)

arr = [3, 6, 5, 0, 8, 2, 1, 9]

def extract_max(arr):
    max = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    max_heapify(arr, 0)
    print(max)

# extract_max(arr)

arr = [9, 6, 8, 2, 1, 4, 3]

def heap_sort(arr):
    max = arr[0]
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, 0, i)
    print(arr)

heap_sort(arr)
        