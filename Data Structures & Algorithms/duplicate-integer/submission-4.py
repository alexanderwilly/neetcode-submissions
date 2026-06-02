from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = dict(Counter(nums))
        counts = list(counter.values())

        for c in counts:
            if c > 1:
                return True
        
        return False
        