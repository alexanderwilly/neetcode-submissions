import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cpy = []
        hm = {}

        for s in strs:
            cpy.append(''.join(sorted(s)))
        
        for s in cpy:
            if s not in hm:
                hm[s] = []


        for s in strs:
            k = ''.join(sorted(s))
            hm[k].append(s)

        # print(hm.values())

        return list(hm.values())


        