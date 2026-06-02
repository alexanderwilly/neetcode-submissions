class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        for c in s:
            if not c.isalnum():
                s = s.replace(c, "")

        return s == s[::-1]