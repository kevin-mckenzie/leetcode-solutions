'''
First iteration that needs cleaning up. Using a dictionary to count the characters in t and and int to keep track of the number of 
characters whos count has been met, then closing the window until the counts no longer match
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == s:
            return s
        
        t_ct = dict()
        for c in t:
            t_ct[c] = t_ct.get(c, 0) + 1
        
        res = ""
        reslen = float('inf')
        lo = 0
        window = dict()
        c_in_window = 0
        for i, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            
            if (c in t_ct) and (window[c] == t_ct[c]): 
                c_in_window += 1
                
            while c_in_window == len(t_ct):
                if len(s[lo:i+1]) < reslen:
                    res = s[lo:i+1]
                    reslen = i - lo + 1

                window[s[lo]] -= 1
                if (s[lo] in t_ct) and (window[s[lo]] < t_ct[s[lo]]):
                    c_in_window -= 1
                lo += 1
            
        return res

'''
Cleaned up version
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_ct = dict()
        for c in t:
            t_ct[c] = t_ct.get(c, 0) + 1
        
        window = dict()
        have, need = 0, len(t_ct)
        res, lenres = "", float('inf')
        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if (c in t_ct) and (t_ct[c] == window[c]):
                have += 1
            while have == need:
                if (r - l + 1) < lenres:
                    lenres = r - l + 1
                    res = s[l:r+1]
                window[s[l]] -= 1
                if (s[l] in t_ct) and (window[s[l]] < t_ct[s[l]]):
                    have -= 1
                l += 1
        return res