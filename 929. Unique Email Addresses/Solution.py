class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ans = []
        for email in emails:
            local, domain = email.split("@")
            local_modified = []
            for ch in local:
                if ch.isalnum():
                    local_modified.append(ch)
                elif ch == ".":
                    continue
                elif ch == "+":
                    break
            local_modified = "".join(local_modified)
            ans.append(local_modified + "@" + domain)
        return len(set(ans))