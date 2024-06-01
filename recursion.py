def print_name(num):
    while num > 0:
        print('fathima')
        return print_name(num-1)

def print_numbers(start, stop):
    while start <= stop:
        print(start)
        return print_numbers(start+1, stop)
    return

def print_reverse_numbers(start, stop):
    while stop >= start:
        print(stop)
        return print_reverse_numbers(start, stop-1)
    return

def print_backtrack(start, stop):
    if start > stop:
        return
    
    print_backtrack(start+1, stop)
    print(start)

def sum_parameterized(num, sum):
    if num < 1:
        return
    print(sum)
    sum_parameterized(num-1, sum+num)

def sum_functional(num):
    if num == 0:
        return 0
    return num + sum_functional(num-1)

def find_factorial(num):
    if num == 1:
        return 1
    return num * find_factorial(num-1)

def reverse(i, j, arr):
    if i >= j:
        return arr
    arr[i], arr[j] = arr[j], arr[i]
    return reverse(i+1, j-1, arr)

def reverse_1pointer(i,arr,n):
    if i == n//2:
        return arr

    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    return reverse_1pointer(i+1, arr, n)

def palindrome(string, n, i):
    if i >= n/2:
        return True
    
    if string[i] != string[n-1-i]:
        return False
    else:
        return palindrome(string, n, i+1)
    

string = "MADAM"
print(palindrome(string, 5, 0))
arr = [1,2,3,4,5,6,7,8]
n = len(arr)
print(reverse_1pointer(0, arr,n))
# print(reverse(0, 5, [1,2,3,4,5,6]))

# print(sum_functional(3))
# print(find_factorial(4))