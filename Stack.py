#step:1: define a class for stack

class Stack:
    def __init__(self):
        self.stack=[]

    #push in stack
    def push(self,value):
        if value not in self.stack:
            self.stack.append(value)
            print("Pushed {} in the Stack".format(value))
            return True
        else:
            return False

    #pop from stack
    def pop(self):
        if len(self.stack)>0:
            self.stack.pop()
            print("Popped the top element")
        else:
            print("No element in the stack")

    # showing the stack
    def showtop(self):
        return self.stack[-1]

    #showing the stack
    def showstack(self):
        return self.stack[::-1]


stack=Stack()
stack.push("Mon")
stack.push("Tue")
stack.push("Wed")

print(stack.showstack())

stack.pop()
print(stack.showstack())