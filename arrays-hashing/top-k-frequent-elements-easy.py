class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        num_ct maps each number in n to the number of times it has been seen
        ct_num maps the count of each number to a set of numbers that have that count.
        ct_num is iterated over at the end in order to find the highest counts and add them to res of length k
        I think it is O(n) because we iterate over nums a max of 2n times, and dictionary and set lookups, removals, and additions are constant time.
        Memory i think is also 2n, which I was thinking of reducing but all my submissions are 99%+ on memory so I think this is ok.
        """
        num_ct = dict()
        ct_num = dict()
        res = []
        for n in nums:
            num_ct[n] = num_ct.get(n, 0) + 1
            if num_ct[n] in ct_num:
                ct_num[num_ct[n]].add(n)
            else:
                ct_num[num_ct[n]] = set([n])
            if num_ct[n] - 1 > 0:
                ct_num[num_ct[n] - 1].remove(n)

        for i in range(len(nums), 0, -1):
            if i in ct_num:
                for n in ct_num[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
        return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Solution 2:
        by iterating over nums and getting the counts first, then mapping each count a list of frequencies, 
        only one dictionary is necessary. For some reason this uses more memory in practices, though. 
        Also, this is 3n time instead of 2n which is negligible but worth mentioning
        """
        res = []
        ct = {}
        
        for n in nums:
            ct[n] = 1 + ct.get(n, 0)
            
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in ct:
            freq[ct[n]].append(n)
        
        
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res