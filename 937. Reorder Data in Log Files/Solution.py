class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters = []
        digits = []
        
        for log in logs:
            if log.split(" ")[1].isalpha():
                letters.append(log)
            else:
                digits.append(log)
        
        def weird_sort(log):
            log_letters = log.split(" ")
            identifier, letter = log_letters[0], log_letters[1:]
            return " ".join(log_letters[1:]) + identifier
        
        letters.sort(key=weird_sort)
        
        return letters + digits