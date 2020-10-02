class Solution:
    def compress(self, chars: List[str]) -> int:
        anchor = write = 0
        for idx, ch in enumerate(chars):
            if idx + 1 == len(chars) or chars[idx + 1] != ch:
                chars[write] = chars[anchor]
                write += 1
                if idx > anchor:
                    for digit in str(idx - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = idx + 1
        return write