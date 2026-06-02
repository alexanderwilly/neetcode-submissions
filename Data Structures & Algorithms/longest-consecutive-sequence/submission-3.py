class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        
        distincts = list(set(nums))
        distincts.sort()
        print(distincts)

        longest_count = 0
        c = 1

        for i in range(1, len(distincts)):
            if distincts[i] == distincts[i-1] + 1: # if consecutive
                c += 1
                print(c)
            else:
                longest_count = max(c, longest_count)
                c = 1
        
        longest_count = max(c, longest_count)
                

        return longest_count

        