class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.defaultdict(int)
        for task in tasks:
            freq[task] += 1
        lst = sorted(freq.values(), reverse=True)
        count = 0
        i = 0
        while i < len(lst) - 1:
            if lst[i] == lst[i + 1]:
                count += 1
            else:
                break
            i += 1
        most_letter = lst[0]
        length = len(tasks)
        if count >= n:
            return length
        slots = (n - count) * (most_letter - 1)
        rest = length - most_letter * (count + 1)
        if rest >= slots:
            return length
        else:
            return n * (most_letter - 1) + most_letter + count