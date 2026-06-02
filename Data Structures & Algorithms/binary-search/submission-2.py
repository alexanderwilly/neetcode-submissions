class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        # [-1,0,2,4,6,8]
        # l = 0
        # r = 5
        # i = (0+5)//2 = 2 --> 2

        # l = 3
        # r = 5
        # i = (3+5)//2 = 4 --> 6

        # l = 3
        # r = 4


        while l <= r:
            i = l + ((r - l) // 2)

            # check if middle point is the target
            if nums[i] == target:
                return i
            else:
                # if not equal, check if the middle point is larger or smaller than
                # target
                # if target is smaller, then look at the left sublist (change r to i-1)
                # if target is larger, then look at the right sublist (change l to i+1)
                if target < nums[i]:
                    r = i-1
                else:
                    l = i+1
        
        return -1

