class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            #outer if block determines how to treat mid for the inner if block
            if nums[mid] < nums[lo]:
                #now determine which half of the array has target in it. need to or because one or both conditions are needed 
                if nums[mid] > target or target > nums[hi]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target or target < nums[lo]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1