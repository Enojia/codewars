import re

def longest_pallindrome(s):
    pattern = re.finditer(r"((.)\2)",s)
    indices = [m.start(0) for m in pattern]  ## finding indices of two consecutive letters
    counts = []

    for ind in indices:
        i = ind - 1
        j = ind + 2
        num = 2
        while( i >= 0 and j < len(s)):
            if s[i] != s[j]:
                break
            else:
                num += 2
                i-=1
                j+=1
        counts.append(num)

    return max(counts)

print longest_pallindrome('baa')
