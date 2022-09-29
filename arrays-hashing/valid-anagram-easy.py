"""
This first solution uses two dicts and uses alot of memory and is slow
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = dict()
        t_count = dict()
        
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1
            
        for c in s:
            if s_count.get(c, 0) != t_count.get(c, 0):
                return False
            
        return True

"""
This solution uses only one dict, saving memory.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = dict()
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
            
        for c in s:
            if count[c] != 0:
                return False
                    
        return True

"""
This solution iterates of s and t separately, allowing for iteration of t to exit sooner if a character is not found
and save a lot of time. The time saving appears to be related to the use of .get() as adding it in lieu of lines 
50-53 slows this solution back down again significantly. Memory is about the same.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()
        for l in s:
            if l in letters: #letters[l] = letters.get(l, 0) + 1 is much slower
                letters[l] += 1
            else:
                letters[l] = 1
        for l in t:
            if l in letters:
                letters[l] -= 1
            else:
                return False
        for ct in letters.values():
            if ct != 0:
                return False
        return True