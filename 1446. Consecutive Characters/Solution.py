class Solution:
    def maxPower(self, s: str) -> int:
        i = 1
        power = 1
        repeat = 1
        while i < len(s):
            if s[i - 1] == s[i]:
                repeat += 1
            else:
                power = max(power, repeat)
                repeat = 1
            i += 1
        power = max(power, repeat)
        return power


# Provided solution
class Solution:
    def maxPower(self, s: str) -> int:
        count = 0
        max_count = 0
        previous = None
        for c in s:
            if c == previous:
                # if same as previous one, increase the count
                count += 1
            else:
                # else, reset the count
                previous = c
                count = 1
            max_count = max(max_count, count)
        return max_count