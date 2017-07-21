class stack(object):

    def __init__(self):
        self.items = []


    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items += [item]

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def balance_check(s):
    stk = stack()
    for i in range(len(s)):
        if s[i] == ")":
            if stk.pop() != "(":
                return False
        elif s[i] == "]":
            if stk.pop() != "[":
                return False
        elif s[i] == '}':
            if stk.pop() != "{":
                return False
        else:
            stk.push(s[i])
    return stk.isEmpty()


### Testing Balance_check
print balance_check('[]')
print balance_check('[](){([[[]]])}')
print balance_check('()(){]}')

