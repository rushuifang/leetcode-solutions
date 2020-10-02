# class RecentCounter:

#     def __init__(self):
#         self.storage = []

#     def ping(self, t: int) -> int:
#         self.storage.append(t)
#         while self.storage:
#             if t-3000 > self.storage[0]:
#                 self.storage.pop(0)
#             else:
#                 break
#         return len(self.storage)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# Hints: python list: remove element while looping can cause error
storage = [3009, 100, 3001, 3999, 4444, 3002, 30]
minus_lim = 2
plus_lim = 3002

idx = 0
while True:
    if idx == len(storage):
        break
    el = storage[idx]
    if el >= minus_lim and el <= plus_lim:
        idx += 1
    else:
        storage.remove(el)
print(idx)
print(storage)