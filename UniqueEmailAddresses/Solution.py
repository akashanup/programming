class Solution:
    def processEmail(self, email):
        email = email.split('@')
        email[0] = email[0].split('+')
        email[0][0] = email[0][0].replace('.', '')
        return email[0][0] + '@' + email[1]

    def numUniqueEmails(self, emails: List[str]) -> int:
        emailHashSet = set()
        for email in emails:
            emailHashSet.add(self.processEmail(email))
        return len(emailHashSet)


