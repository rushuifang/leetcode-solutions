class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_buffer = []
        word_count = defaultdict(int)
        max_count = 0
        ans = ""
        for idx, ch in enumerate(paragraph):
            if ch.isalpha():
                word_buffer.append(ch.lower())
                if idx < len(paragraph) - 1:
                    continue
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                if word not in banned:
                    word_count[word] += 1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word
                word_buffer = []
        return ans