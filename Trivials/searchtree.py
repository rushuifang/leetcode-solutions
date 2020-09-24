class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data > data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif self.data < data:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

    def findVal(self, val):
        if self.data > val:
            if self.left is None:
                return str(val) + " not found"
            else:
                return self.left.findVal(val)
        elif self.data < val:
            if self.right is None:
                return str(val) + " not found"
            else:
                return self.right.findVal(val)
        else:
            return str(val) + " found"

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
# print(root.insert(7))
# root.printTree()
print(root.findVal(7))
print(root.findVal(14))