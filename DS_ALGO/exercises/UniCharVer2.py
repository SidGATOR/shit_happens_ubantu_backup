def uni_char(s):

    if len(s) == 0:
        return True

    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)

    return True

