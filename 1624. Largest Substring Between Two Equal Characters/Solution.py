class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        letters = []
        for el in freq.items():
            if el[1] > 1:
                letters.append(el[0])
        
        maxSubstring = 0
        n = len(s)
        if not letters:
            return -1
        for letter in letters:
            maxSubstring = max(maxSubstring, n - s[::-1].index(letter) - s.index(letter) - 2)
        return maxSubstring

# I thought too much, this is how it should be done:

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
	
		# init a default dict, 'd', so we can directly access it d[x] and it will return an empty list []
        d = collections.defaultdict(list)
		
		# List comprehension
		# Build a mapping of 'character' to list of 'index'
		# {'c' : [0, 3, 5]} as an example
        [d[c].append(idx) for idx, c in enumerate(s)]
		
		# The result we want to return
        result = 0
		
		# Enumerate over items
        for key, items in d.items():
		
			# Update max result
            result = max(result, items[-1] - items[0])
			
		# Return result
        return result-1
