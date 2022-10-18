

'''
By starting at beginning and end, can increment inward based on the smaller of each pair of heights,
because at the furthest distance this is guarenteed to be the greatest volume for that smaller height.
If heights are equal, increment the lower pointer.
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        lo, hi, res = 0, len(height) - 1, 0
        
        while lo < hi:
            res = max(res, (hi - lo) * min(height[hi], height[lo]))
            if height[hi] < height[lo]:
                hi -= 1
            else:
                lo += 1
                
        return res