

'''
Solution using dict to store indices of each integer so that lo can quickly be changed to the next value if a repeating character is found.
Faster, but worse on memory because of the dict.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_sub = 0
        lo = 0
        c_sub = dict()
        
        for i, n in enumerate(s):
            if n in c_sub and lo <= c_sub[n]:
                lo = c_sub[n] + 1 

            l_sub = max(l_sub, i - lo + 1)
            c_sub[n] = i
        
        return l_sub

'''
Using a set, when a repeated value is found simply remove every value in the window until the repeated character is removed.
This solution has cleaner variable naming but I think the logic is a little harder to follow.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = set()
        l = 0
        res = 0
        
        for i in range(len(s)):
            
            while s[i] in window:
                window.remove(s[l])
                l += 1
                
            window.add(s[i])
            
            res = max(res, i - l + 1)
                
        
        return res
            