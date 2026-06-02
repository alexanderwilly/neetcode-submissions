from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_s = Counter(s)
        hm_t = Counter(t)
        

        return hm_s == hm_t
        