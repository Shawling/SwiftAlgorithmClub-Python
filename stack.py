""" 栈的实现，注意栈的大小限制
"""

class Stack(object):

    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) > self.limit:
            raise StackOverFlowError
        self.stack.append(data)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from empty')

    def peek(self):
        if self.stack:
            return self.stack[-1]


class StackOverFlowError(BaseException):
    pass


if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print(stack.peek())
    print(stack.pop())
    print(stack.peek())