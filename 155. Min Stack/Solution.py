class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.storage = []
        self.min = [float("inf")]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.storage.append(x)
        if x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.min[-1] == self.storage.pop():
            self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.storage[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()