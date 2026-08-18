class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums)-1
        while l < r: # last value left is the minimum
            mid = (r + l) // 2
            if nums[r] >= nums[mid]: # right side sorted so minimum is either mid or on left.
                r= mid
            else :
                 l = mid+1

        return nums[l]
