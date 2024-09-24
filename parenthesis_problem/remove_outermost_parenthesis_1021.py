s = "()(())"

ans = ""
count = 0

for ch in s:
    if ch == '(':
        if count :
            ans += ch
        count += 1
    else:
        count -= 1
        if count :
            ans += ch

print(ans)
    