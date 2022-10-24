class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for p in s:
            if p in p_map.values():
                stack.append(p)
            elif p in p_map.keys() and len(stack) > 0 and stack[-1] == p_map[p]:
                stack.pop(-1)
            else:
                return False
        return len(stack) == 0