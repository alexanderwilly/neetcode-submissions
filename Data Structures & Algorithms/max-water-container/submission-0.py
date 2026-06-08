class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        res = 0

        while l != r:
            # area = width * height
            area = (r-l) * min(heights[r], heights[l])
            res = max(res, area)

            # move smallest pointer
            # if left pointer is small, then move left pointer
            if heights[l] < heights[r]:
                l = l+1
            # if right pointer is small, then move right pointer
            else:
                r = r-1
        
        return res