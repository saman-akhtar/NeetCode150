class Solution:

    # Claryfing q ow many @ ?
    # empty check
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            part = email.split('@')
            local = part[0]
            domain = part[1]
            local = local.split('+')[0]
            local = local.replace(".", "")
            new_email = local + "@" + domain
            unique.add(new_email)
        return len(unique)

# TC O(N * M)
# SC O(N)