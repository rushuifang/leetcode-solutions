class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def final_str(s):
            stack = []
            i = 0
            while i < len(s):
                if s[i].isalpha():
                    stack.append(s[i])
                else:
                    if stack:
                        stack.pop()
                i += 1
            return "".join(stack)
        return final_str(S) == final_str(T)

# O(1) space
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))