class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1
        while hi > lo:
            while (not s[lo].isalnum()) and (lo < hi):
                lo += 1
            while (not s[hi].isalnum()) and (hi > lo):
                hi -= 1
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1  
        return True
        