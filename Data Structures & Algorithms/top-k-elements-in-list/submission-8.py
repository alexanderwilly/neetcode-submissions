from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = dict(Counter(nums))
        s = dict(sorted( c.items(), key = lambda x: x[1], reverse = True ))
        return list(s.keys())[:k]
        