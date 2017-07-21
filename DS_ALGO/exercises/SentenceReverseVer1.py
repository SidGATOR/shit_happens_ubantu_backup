def rev_word(s):
    s = s.split()
    s_rev = ''
    for item in s[::-1]:
        s_rev += item + " "
    return s_rev[:-1]
