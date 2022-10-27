'''
Using same logic as search in rotated sorted array, split the array in half according to which side the 
wraparound from hi to lo happens in.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            #the following check is the hardest part of the problem. Depending on odd/even length and the location of the minimum, either of these may be the answer.
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[lo] < nums[lo - 1]:
                return nums[lo]
            
            if nums[mid] < nums[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
        return nums[mid]