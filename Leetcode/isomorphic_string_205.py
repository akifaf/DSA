

s = "oooa"
t = "eeef"

def isomorphic(s, t):
    mapS = {}
    mapT = {}

    for i in range(len(s)):

        if (s[i] in mapS and mapS[s[i]] != t[i]) or (t[i] in mapT and mapT[t[i]] != s[i]):
            return print(False)

        mapS[s[i]] = t[i]
        mapT[t[i]] = s[i]

    return print(True)


    
isomorphic(s,t)