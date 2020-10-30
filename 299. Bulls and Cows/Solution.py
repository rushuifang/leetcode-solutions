class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        i = 0
        bulls, cows = 0, 0
        while i < len(secret):
            if secret[i] == guess[i]:
                bulls += 1
                secret = secret[:i] + secret[i + 1 :]
                guess = guess[:i] + guess[i + 1 :]
            else:
                i += 1
        secrets = [el for el in secret]
        guesses = [el for el in guess]
        j = 0
        while j < len(secrets):
            if secrets[j] in guesses:
                cows += 1
                guesses.remove(secrets[j])
                secrets.remove(secrets[j])
            else:
                j += 1
        return str(bulls) + "A" + str(cows) + "B"
