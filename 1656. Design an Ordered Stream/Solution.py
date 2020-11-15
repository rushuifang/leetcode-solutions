class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = ["" for _ in range(n)]
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id-1] = value
        res = []
        if self.ptr == id:
            while id <= self.n and self.stream[id-1] != "":
                res.append(self.stream[id-1])
                id += 1
            self.ptr = id
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)