import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '').lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
