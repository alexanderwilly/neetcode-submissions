from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in hm:
                hm[sorted_str] = [s]
            else:
                hm[sorted_str].append(s)
        
        res = []
        for k, v in hm.items():
            res.append(v)


        return res
        