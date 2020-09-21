class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class singlyLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        printVal = self.head
        while printVal:
            print(printVal.val)
            printVal = printVal.next

    def addBeginning(self, newData):
        e = Node(newData)
        e.next = self.head
        self.head = e

    def addEnd(self, newData):
        e = Node(newData)
        if not self.head:
            self.head = e
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = e

    def addMiddle(self, middleNode, newData):
        e = Node(newData)
        if not middleNode:
            print("Invalid node")
            return
        e.next = middleNode.next
        middleNode.next = e

    def removeNode(self, oldData):
        headNode = self.head
        if not headNode:
            return
        if headNode.val == oldData:
            self.head = headNode.next
            return
        while headNode:
            if headNode.val == oldData:
                break
            prevNode = headNode
            headNode = headNode.next
        if not headNode:
            return
        prevNode.next = headNode.next
        headNode = None


List1 = singlyLinkedList()
List1.head = Node("Monday")
d2 = Node("Tuesday")
d_out = d2
d3 = Node("Wednesday")
d4 = Node("Thursday")
d5 = Node("Friday")
List1.head.next = d2
d2.next = d3
d3.next = d4
d4.next = d5

# if assign d_out = d_out.next, it doesn't affect d2
# d_out = d_out.next
# print(d_out.val)
# print(d2.val)

# if assign d_out = d4, it doesn't affect d2
# d_out = d4
# print(d_out.val)
# print(d2.val)

# if d_out.next is changed, then d2.next is changed
# d_out.next = d4
# print(d2.next.val)

# print(List1.head.next.next.val)
# List1.printList()

# List1.addBeginning("Sunday")
# List1.printList()

# List1.addEnd("Saturday")
# List1.printList()

# List1.addMiddle(d3, "Lucky day")
# List1.printList()

# List1.removeNode("Friday")
# List1.printList()