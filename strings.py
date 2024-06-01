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

reverse_sent(sent)
