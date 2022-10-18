
'''
First version of the solution. Very ugly.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2:
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                t_sum = sum([nums[i], nums[lo], nums[hi]])
                if t_sum > 0:
                    hi -= 1
                elif t_sum < 0:
                    lo += 1
                elif t_sum == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == res[-1][1]:
                        lo += 1
            i += 1
            print(nums[i])
            while i < lo and nums[i - 1] == nums[i]:
                i += 1
        return res

'''
Second, slightly cleaner version
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                t_sum = nums[i] + nums[lo] + nums[hi]
                if t_sum < 0:
                    lo += 1
                elif t_sum > 0:
                    hi -= 1
                elif t_sum == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    while lo < hi and nums[lo -1] == nums[lo]:
                        lo += 1
        return res