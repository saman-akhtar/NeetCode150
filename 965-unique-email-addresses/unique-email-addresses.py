class Solution:

    # Claryfing q ow many @ ?
    # empty check
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace(".", "")
            new_email = local + "@" + domain
            unique.add(new_email)
        return len(unique)

# TC O(N * M)
# SC O(N)