def compress(s):
    ret_s = ''
    seen = {}

    for i in range(len(s)):
        if s[i] not in seen:
            seen[s[i]] = 1
        else:
            seen[s[i]] += 1

    for key in sorted(seen):
        ret_s += key + str(seen[key])

    return ret_s

print (compress('AAAAABBBBCCCC'))
