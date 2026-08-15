class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width = min wall height * index difference
        l = 0 
        r = len(heights)-1
        max_width = 0

        while l < r:
            width = min(heights[l], heights[r]) *(r-l)
            max_width = max(max_width, width)
            if heights[l] < heights[r]: l+=1
            else: r-=1
        return max_width    
