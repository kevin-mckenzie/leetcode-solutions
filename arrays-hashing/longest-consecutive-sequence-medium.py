class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_seq = 0
               
        for n in nums:
            if n - 1 not in numset:
                cn = n
                cur_seq = 0
                while cn in numset:
                    cur_seq += 1
                    cn += 1
                max_seq = max(max_seq, cur_seq)
                
        return max_seq