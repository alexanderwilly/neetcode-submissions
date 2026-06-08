class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort list
        nums.sort()
        target = 0
        res = []

        for a in range(0, len(nums)-2):
            # check if a has been used previously
            if a > 0:
                if nums[a] == nums[a-1]:
                    continue
                # else use "a"
            # else use "a"

            l = a + 1
            r = len(nums)-1
            remaining = target - nums[a]

            while l < r:
                current_sum = nums[l] + nums[r]
                # if (l + r) result is smaller < than remaining... increase left
                # if (l + r) result is larger > than remaining... decrease right
                if current_sum < remaining:
                    l = l+1
                elif current_sum > remaining:
                    r = r-1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    l = l+1
                    
                    # Prevent using the same left pointer value
                    while nums[l] == nums[l-1] and l < r:
                        l = l+1
                            


        return res