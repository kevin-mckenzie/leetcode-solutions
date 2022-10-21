
'''
Sliding window technique while tracking the main character in the window and closing the window and updating
maxf when a different character is encountered.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lo = 0
        maxf = 0
        res = 0
        window = dict()
        
        for i, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            maxf = max(maxf, window[c])
            while (maxf + k ) < (i - lo + 1):
                window[s[lo]] -= 1
                lo += 1
            
            res = max(res, i - lo + 1)
                      
        return res