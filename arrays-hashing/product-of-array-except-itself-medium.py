class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = nums.copy()
        right = nums.copy()        
        for i in range(1, len(nums)):
            left[i] *= left[i - 1]
            right[-i-1] *= right[-i]
        
        res = [0] * len(nums)
        res[0], res[-1] = right[1], left[-2]

        for i in range(1, len(nums)-1):
            res[i] = left[i-1] * right[i+1]
            
        return res

'''
This solution saves memory by tracking the products as ints instead of arrays and updatint ans ans as nums is iterated over
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1 for i in range(len(nums))]
        
        l, r = 1, 1
        
        for i in range(len(nums)):
            ans[i] *= l
            ans[-i - 1] *= r
            l *= nums[i]
            r *= nums[-i - 1]
        
        return ans