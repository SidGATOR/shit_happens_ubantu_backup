def anagram_chk(test,data):
    test = test.lower()
    data = data.lower()
    test = list(''.join(test.split(' ')))
    data = list(''.join(data.split(' ')))
    #print (test,data)
    if len(data) != len(test):
        return False
    else:
        chk = True
        while(len(test) > 0 and chk == True):
            chk = False
            if test[0] in data:
                chk = True
                del test[0]
        return chk

test = ["public relations", "clint eastwood"]
data = ["crap built on lies", "old west action"]
for i in range(len(test)):
    print(anagram_chk(test[i],data[i]))
