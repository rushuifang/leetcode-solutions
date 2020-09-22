class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        self.stack.append(data)
        return

    def remove(self):
        if len(self.stack):
            self.stack.pop()
        else:
            print("No elements to be removed!")
            return


stack1 = Stack()
stack1.add("Monday")
stack1.add("Tuesday")
stack1.remove()
stack1.remove()
stack1.remove()
# print(stack1.stack)