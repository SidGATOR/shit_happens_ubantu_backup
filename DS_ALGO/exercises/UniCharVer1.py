def uni_char(s):
    
    if len(s) == 0:
        return True
    
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            return False
    
    return True
