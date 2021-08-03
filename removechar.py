def delchar(s, c):
    str=""
    if len(c) == 1:
        for i in range(len(s)):
            if s[i] != c:
                str = str + s[i]
        return str
    else:
        return s


print(delchar("banana", 'nn'))
