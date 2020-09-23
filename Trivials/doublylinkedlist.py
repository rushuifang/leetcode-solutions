class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class doublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode
        self.head = newNode

    def printList(self, node):
        while node:
            print(node.data)
            last = node
            node = node.next

    def insert(self, prevNode, data):
        if not prevNode:
            return
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode

    def append(self, data):
        newNode = Node(data)
        newNode.next = None
        if not self.head:
            newNode.next = None
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
        newNode.prev = last
        return


# dllist = doublyLinkedList()
# dllist.push(12)
# dllist.push(8)
# dllist.push(62)
# dllist.printList(dllist.head)

# dllist.insert(dllist.head.next, 13)
# dllist.printList(dllist.head)

dllist = doublyLinkedList()
dllist.push(12)
dllist.append(9)
dllist.push(8)
dllist.push(62)
dllist.append(45)
dllist.printList(dllist.head)