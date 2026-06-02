class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for n in nums:
                hm[n] = 1 + hm.get(n, 0)
        
        my_set = []
        for key, val in hm.items():
            my_set.append((val, key))

        my_set.sort(reverse = True)

        res = []
        for i in range(k):
            res.append( my_set[i][1] )

        return res
        