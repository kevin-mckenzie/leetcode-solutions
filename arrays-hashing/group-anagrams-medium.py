class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        
        for s in strs:
            s_sorted = tuple(sorted(list(s))) #use tuple of sorted string as hash value, would need hash function to handle longer strings, but 100 largest possible for this problem
            if not (s_sorted, len(s)) in hashmap:
                hashmap[(s_sorted, len(s))] = []
            hashmap[(s_sorted, len(s))].append(s)
        
        return hashmap.values()