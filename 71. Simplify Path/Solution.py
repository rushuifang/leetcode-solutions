class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        word = ""
        stack = []
        for i in range(len(path)):
            if path[i].isalpha():
                word += path[i]
            else:
                if word:
                    stack.append(word)
                    word = ""
                else:
                    if path[i] == "." and i != len(path) - 1 and path[i + 1] == "." and stack:
                        stack.pop()
        return "/" + "/".join(stack)

# The first one doesn't do with more than 2 dots

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        symbols = path.split("/")
        ans = []
        for symbol in symbols:
            if symbol == ".." and ans:
                ans.pop()
            elif symbol == "" or symbol == "." or (symbol == ".." and not ans):
                continue
            else:
                ans.append(symbol)
        print(ans)
        return "/" + "/".join(ans)
            
    # Second one can be more simplified
class Solution:
    def simplifyPath(self, path: str) -> str:
        r = []
        for s in path.split('/'):
            r = {'':r, '.':r, '..':r[:-1]}.get(s, r + [s])
        return '/'+'/'.join(r)