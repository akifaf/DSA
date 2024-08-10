word = 'rattratt'

def symmentric(word):
    n = len(word) 
    if n % 2 != 0:
        return "Not symmetric"
    j = len(word)//2
    for i in range(n//2):
        if word[i] != word[j]:
            return "Not symmetric"
        else:
            j += 1
    
    return "Symmetric"

sent = "my name is fathima"

def reverse_sent(sent):
    sent = sent.split()
    sent = sent[::-1]
    result = " ".join(sent)
    print(result)

# reverse_sent(sent)

def reverse_int(num):
    neg = False
    if num < 0:
        num *= (-1)
        neg=True
    result = 0
    while num>0 :
        digit = num%10
        result = (result * 10) + digit
        num = num // 10
    
    return result if neg==False else -result

# print(reverse_int(-23400))
import math
def reverse_integer(num):
    result =0
    while num != 0:
        digit = num%10 if num>0 else num%-10
        result = (result*10) + digit
        num = math.trunc(num/10)

    return result

# print(reverse_integer(-123))

def largestOddNum(num):
    for i in range(len(num)-1, -1,-1):
        # print(num[i], 'num')
        if int(num[i]) % 2 != 0:
            # print(num[i])
            return print(num[:i+1])
        
    return print('')

# largestOddNum("123234234")

def palindrome(num):
    org_num = num
    reverse =  0
    while num>0:
        digit = num%10
        reverse = reverse*10 + digit
        num //= 10
    return True if org_num==reverse else False
    

print(palindrome(242))