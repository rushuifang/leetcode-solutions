class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            elif self.data < data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data


# e = Node(10)
# e.printTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.printTree()