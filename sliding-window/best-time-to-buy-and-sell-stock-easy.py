
'''\
Track minimum seen up to any point then the maximum that occurs after that miniumum to get the max profit.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cmin, maxp = 10**4 + 1, 0
        
        for p in prices:
            cmin = min(cmin, p)
            maxp = max(maxp, p - cmin)
            
        return maxp