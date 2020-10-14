class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        L = []
        for word in words:
            morse_code = ""
            for ch in word:
                morse_code += MORSE[ord(ch) - ord("a")]
            L.append(morse_code)
        return len(set(L))
