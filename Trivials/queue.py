class Queue:
    def __init__(self):
        self.queue = []

    def add(self, data):
        self.queue.insert(0, data)
        return

    def remove(self):
        if len(self.queue):
            self.queue.pop()
        else:
            print("No elements to be removed")
        return


queue1 = Queue()
queue1.add("Monday")
queue1.add("Tuesday")
queue1.remove()
queue1.remove()
queue1.remove()
print(queue1.queue)