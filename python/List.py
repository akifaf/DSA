# def countNoOfPalindrome(word):
#     subs = []
#     result = 0
#     for i in range(len(word)):
#         for j in range(i, len(word)):
#             check = word[i:j+1]
#             if len(check) > 1:
#                 if check == check[::-1]:
#                     print(check)
#                     result += 1

#     return print(result)

# # countNoOfPalindrome('racecarradarslmalayalam')

# def outer(func):
#     def inner(a,b):
#         if a < b:
#             a, b = b, a
#         return func(a, b)
#     return inner

# @outer
# def divide(a, b):
#     return a/b

# # print(divide(2, 4))


# class Students:

#     school = "MES"

#     def __init__(self):
#         self.class_no = 1
#         self.section = "A"

# A1 = Students()
# A2 = Students()

# print(A1.class_no)
# A1.class_no = 2
# Students.school = "HELLO"
# print(A1.school, 'A1')
# print(A2.school, 'A2')
# print()



# numbers = [1, 2, 3, 5, 6]

# for i in range(1, len(numbers)+1):
#     if numbers[i-1] != i:
#         print(i)
#         break
# else:
#     print(i)


numbers = [1, 3, 2, 2, 4, 0, 5]
target = 5


numbers = [ 10, 22, 9, 33, 21, 50, 41, 60]

def logest_increasing_subsequence(arr):

    pass

words = ["listen", "silent", "enlist", "inlets", "google", "cat", "act", "tac"]
target = "silent"

def find_anagram(words, target):
    result = []
    target_dict = {}

    for i in target:
        target_dict[i] = target_dict.get(i, 0) + 1

    for word in words:

        word_dict = {}

        for letter in word:

            word_dict[letter] = word_dict.get(letter, 0) + 1
            
        
        if word_dict == target_dict:
            result.append(word)

    return print(result)


# find_anagram(words, target)

numbers = [1, 2, 3, 4, 5]
k = 2

def rotate_right(numbers, k):

    n = len(numbers)
    k = k % n

    numbers.reverse()

    numbers[:k] = reversed(numbers[:k])
    numbers[k:] = reversed(numbers[k:])


    return print(numbers)

# rotate_right(numbers, k)


numbers = [1, 2, 3, 4, 2, -1]
target_sum = 5

# [[2, 3], [3, 2], [1, 2, 3, -1]]  # output

def subarray_sum_target(numbers, target):

    result = []

    for i in range(len(numbers)):

        sum = 0

        for j in range(i, len(numbers)):

            sum += numbers[j]
            print(sum)
            if sum == target:
                arr = numbers[i:j+1]
                result.append(arr)

    return print(result)
    
# subarray_sum_target(numbers, target_sum)


numbers = [100, 4, 200, 1, 3, 2]

n = [1, 2, 3, 4, 100, 200]

def longest_consecutive_sequence(numbers):
    pass

numbers = [2, 4, 3, 5, 7, 8, 1, 9]
target_sum = 10

def pair_sum(numbers, target):

    result = set()
    pair = set()
    
    

# pair_sum(numbers, target_sum)

numbers = [1, 2, -3, 4, -2, -1, 0, 5]
target_sum = 3

# x + y + z = target

# x - target + y = -z

def triplet_sum(numbers, target):
    
    result = []

    for x in range(len(numbers)):
        ans = numbers[x] - target
        for y in range(x+1, len(numbers)):
            target_num = ans + y
            if target_sum in numbers:
                answer = (x, y, target_sum)
                result.append(answer)

    return result

print(triplet_sum(numbers, target_sum))